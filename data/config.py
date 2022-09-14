import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
GENERAL_ID = 1096151413

admins = [
    1096151413,

]

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
IP = str(os.getenv("IP"))

POSTGRES_URL = f'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'