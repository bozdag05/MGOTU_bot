from utils.db_api.schemas.db_docs import Doc
from utils.db_api.db_mgotu import db
from asyncpg import UniqueViolationError


async def add_doc(build: str, name_file: str, file_url: str):
    try:
        doc = Doc(build=build, name_file=name_file, file_url=file_url)
        await doc.create()

    except UniqueViolationError:
        print('add doc error')


async def select_all_docs():
    docs = await Doc.query.gino.all()
    return docs


async def count_doc():
    count = await db.func.count(Doc.file_url).gino.scalar()
    return count


async def select_doc(name_file):
    doc = await Doc.query.where(Doc.name_file == name_file).gino.first()
    return doc


async def delete_doc(name_file):
    doc = await Doc.query.where(Doc.name_file == name_file).gino.first()
    await doc.delete()


async def select_docs(build):
    docs = await Doc.query.where(Doc.build == build).gino.all()
    return docs


async def update_doc(name_file, new_file_url):
    file = await select_doc(name_file)
    await file.update(file_url=new_file_url).apply()
