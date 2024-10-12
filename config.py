import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables and cast to correct types
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID")) if os.getenv("API_ID") else None
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL")) if os.getenv("LOG_CHANNEL") else None
DB_NAME = os.getenv("DB_NAME")
AUTH_USERS = set(int(x) for x in os.getenv("AUTH_USERS", "").split()) if os.getenv("AUTH_USERS") else set()
DB_URL = os.getenv("DB_URL")
BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True").lower() == 'true'
