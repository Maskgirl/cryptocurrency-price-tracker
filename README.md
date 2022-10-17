# cryptocurrency_price_tracker
Cryptocurrency price tracker in Django

# How to run 

1. Add min-max price values for any number of coins to track for alerting in `cryptocurrency_price_tracker\settings\settings.py`.
   ```python
   COINS_MIN_MAX_MAP = {
        "bitcoin": {
            "min": 19599.10,
            "max": 19599.57
        },
        "litecoin": {
            "min": 51.50,
            "max": 51.69
        }
   }
   ```
2. Added .env file at `cryptocurrency_price_tracker\settings\.env` with following values
    ```commandline
   EMAIL_HOST=<SECRET>
   EMAIL_HOST_USER=<SECRET>
   EMAIL_HOST_PASSWORD=<SECRET>
   EMAIL_PORT=<SECRET>
   FROM_EMAIL=<SECRET>
   TO_EMAIL=<SECRET>
   ALERT_SCHEDULER_SECONDS=30
    ```
3Run following command to run the server 
   ```
   docker compose up
   ```

## APIs

1. `/api/prices/<coin_name>/?date=2022/10/17`
   1. example - `http://127.0.0.1:8000/api/prices/litecoin/?date=2022/10/17`
   