import os

CONFIG = {
    "schedule_interval": int(os.getenv("SCHEDULE_INTERVAL", 5)),
    "mysql": {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USERNAME"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    },
}
