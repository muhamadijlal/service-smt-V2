import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

CONFIG = {
    "db_connection": os.getenv("DB_CONNECTION"),
    "schedule_interval": int(os.getenv("SCHEDULE_INTERVAL", 5)),
    "mysql": {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USERNAME"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    },
    "pgsql": {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USERNAME"),
        "port": int(os.getenv("DB_PORT", 5432)),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    },
}
