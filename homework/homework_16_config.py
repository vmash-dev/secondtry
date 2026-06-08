import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.ukr.net")
USER_UKR_NET = os.getenv("USER")
TOKEN_UKR_NET = os.getenv("TOKEN_UKR_NET")
API_KEY = os.getenv("API_KEY")

print(USER_UKR_NET)
