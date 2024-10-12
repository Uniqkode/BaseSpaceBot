import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
DB_NAME = os.getenv("DB_NAME")
AUTH_USERS = set(int(x) for x in os.getenv("AUTH_USERS").split())
DB_URL = os.getenv("DB_URL")
BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True").lower() == 'true'
