from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def check_prices_runner():
    print("calling....")


def check_price_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_prices_runner, 'interval', seconds=30)
    scheduler.start()
