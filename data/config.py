import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
GENERAL_ID = 

admins = []

lis_build_1 = ['ККМТ', 'ТТД', 'МГОТУ']
lis_build_2 = ["Общежитие №1", "Общежитие №2"]

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
IP = str(os.getenv("IP"))

POSTGRES_URL = f'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'
