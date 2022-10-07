from utils.db_api.schemas.db_docs import Doc
from utils.db_api.db_mgotu import db
from asyncpg import UniqueViolationError


async def add_doc(doc_id: int, build: str, name_file: str, file_url: str):
    try:
        doc = Doc(doc_id=doc_id, build=build, name_file=name_file, file_url=file_url)
        await doc.create()

    except UniqueViolationError:
        print('add doc error')


async def select_all_docs():
    docs = await Doc.query.gino.all()
    return docs


async def count_doc():
    count = await db.func.count(Doc.doc_id).gino.scalar()
    return count


async def select_doc_id(doc_id):
    doc = await Doc.query.where(Doc.doc_id == doc_id).gino.first()
    return doc


async def select_doc(name_file):
    doc = await Doc.query.where(Doc.name_file == name_file).gino.first()
    return doc


async def delete_doc(doc_id):
    doc = await Doc.query.where(Doc.doc_id == doc_id).gino.first()
    await doc.delete()


async def select_docs(build):
    docs = await Doc.query.where(Doc.build == build).gino.all()
    return docs


async def update_doc(name_file, new_file_url):
    file = await select_doc(name_file)
    await file.update(file_url=new_file_url).apply()
