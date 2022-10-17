from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from cryptocurrency_price_tracker.settings import *
from pycoingecko import CoinGeckoAPI
from django.core.mail import send_mail
from .models import *
import enum
cg = CoinGeckoAPI()


class PriceState(enum.Enum):
    above_max = 3
    between_min_max = 2
    below_min = 1


def send_alert_mail(subject, email_message):
    send_mail(
        subject,
        email_message,
        FROM_EMAIL,
        [TO_EMAIL],
        fail_silently=False,
    )


coin_to_price_state_map = {}


def check_prices_runner():
    global coin_to_price_state_map
    coin_names = list(COINS_MIN_MAX_MAP.keys())
    coins_detail = cg.get_price(ids=coin_names, vs_currencies='usd', include_last_updated_at=True)

    for coin_name, coin_price_range in COINS_MIN_MAX_MAP.items():
        price = coins_detail[coin_name]['usd']
        max_limit = coin_price_range['max']

        min_limit = COINS_MIN_MAX_MAP[coin_name]['min']

        curr_price_state = PriceState.between_min_max
        if price > max_limit:
            curr_price_state = PriceState.above_max
        if price < min_limit:
            curr_price_state = PriceState.below_min

        if coin_name not in coin_to_price_state_map:
            coin_to_price_state_map[coin_name] = curr_price_state
            continue

        if coin_to_price_state_map[coin_name] != curr_price_state:
            if curr_price_state == PriceState.above_max:
                subject = f"Alert! It's time to sell {coin_name}!"
                message = f"Alert!, {coin_name} price is {price} USD which is above {max_limit}"
                send_alert_mail(subject, message)
            elif curr_price_state == PriceState.below_min:
                subject = f"Alert! It's time to buy {coin_name}!"
                message = f"Alert!, {coin_name} price is {price} USD which is below {min_limit}"
                send_alert_mail(subject, message)
        utc_timestamp = coins_detail[coin_name]['last_updated_at']
        coin_price = CoinPrice(
            coin=coin_name,
            timestamp=datetime.utcfromtimestamp(utc_timestamp),
            price=price)
        coin_price.save()
        coin_to_price_state_map[coin_name] = curr_price_state
    print(coins_detail)


scheduler = BackgroundScheduler()
scheduler.add_job(check_prices_runner, 'interval', seconds=ALERT_SCHEDULER_SECONDS)
