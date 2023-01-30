# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "24524034"))
API_HASH = os.environ.get("API_HASH", "2576e0b5c6675d1728f71e8241899a9e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6197417600:AAHQI0jw5rZPK5u8Rfx2RwIP0x2sgJraY18")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("854143836")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Linkconvertner")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://shok123:shok123@cluster0.pagmwax.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "854143836")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001670322087")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MG_all_movie_links") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
