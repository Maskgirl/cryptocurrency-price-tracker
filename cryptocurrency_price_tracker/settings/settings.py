from .default import *

import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

COINS_MIN_MAX_MAP = {
    "bitcoin": {
        "min": 19599.10,
        "max": 19599.57
    },
}
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL = env("EMAIL")
FROM_EMAIL = env("FROM_EMAIL")
ALERT_SCHEDULER_SECONDS = 30
