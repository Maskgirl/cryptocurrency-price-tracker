# cryptocurrency_price_tracker
Cryptocurrency price tracker in Django

# How to run 

1. Added .env file at `cryptocurrency_price_tracker\settings\.env` with following values
    ```commandline
   EMAIL_HOST=<SECRET>
   EMAIL_HOST_USER=<SECRET>
   EMAIL_HOST_PASSWORD=<SECRET>
   EMAIL_PORT=<SECRET>
   FROM_EMAIL=<SECRET>
   TO_EMAIL=<SECRET>
   ALERT_SCHEDULER_SECONDS=30
    ```
2. Run following command to run the server 
   ```
   docker compose up
   ```

## APIs

1. `/api/prices/bitcoin/`
   