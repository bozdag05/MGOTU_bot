'''import asyncio
import warnings

from data import config
from utils.db_api import rooms_commands as commands
from utils.db_api.db_mgotu import db


async def test_db():
    await db.set_bind(config.POSTGRES_URL)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_doc('Университет', 'larec', 'https://drive.google.com/drive/my-drive')
    await commands.add_doc('ККМТ', 'covid', )
    await commands.add_doc('ККМТ', 'history', )
    await commands.add_doc('ТТД', 'Alex', )

    users = await commands.select_all_docs()
    print(users)

    count = await commands.count_doc()
    print(count)

    user = await commands.select_doc('covid')
    print(user)

    await commands.update_doc('covid', new_file_url='https://drive.google.com/file/d/1dFYtbY91ahRHsBNCsKhZmR_K-2rN6GV_/view?usp=sharing')
    user = await commands.select_doc('covid')
    print(user)

    rooms = await commands.select_docs('ККМТ')
    print(rooms)

warnings.filterwarnings("ignore", category=DeprecationWarning)
loop = asyncio.get_event_loop()
loop.run_until_complete(test_db())'''

text = 'alekc divanov VlaDimir'
print(text.title())