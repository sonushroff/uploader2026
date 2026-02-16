#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23235144"))
API_HASH = environ.get("API_HASH", "1e2e771c7ca985f9e8c71fdcab65b0ce")
BOT_TOKEN = environ.get("BOT_TOKEN", "8553638362:AAGv3wUX5X33Jl43hAk7Fs2IV1qImNB6d0c")

OWNER = int(environ.get("OWNER", "23235144"))
CREDIT = environ.get("CREDIT", "COURSE WALLAH")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '23235144').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '23235144').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))







