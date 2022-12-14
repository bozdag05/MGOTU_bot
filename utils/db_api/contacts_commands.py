from utils.db_api.schemas.db_contact import Contact
from utils.db_api.db_mgotu import db
from asyncpg import UniqueViolationError


async def add_contact(contact_id: int, build: str, name_men: str, position: str, contact: str):
    try:
        contact = Contact(contact_id=contact_id, build=build, name_men=name_men, position=position, contact=contact)
        await contact.create()

    except UniqueViolationError:
        print("add contact error")


async def select_all_contacts():
    contacts = await Contact.query.gino.all()
    return contacts


async def count_contact():
    count = await db.func.count(Contact.contact_id).gino.scalar()
    return count


async def select_contact_id(contact_id):
    contact = await Contact.query.where(Contact.contact_id == contact_id).gino.first()
    return contact


async def select_contact(contact):
    contact = await Contact.query.where(Contact.contact == contact).gino.first()
    return contact


async def delete_contact(contact_id):
    pos = await Contact.query.where(Contact.contact_id== contact_id).gino.first()
    await pos.delete()


async def select_contacts(build):
    contacts = await Contact.query.where(Contact.build == build).gino.all()
    return contacts


async def update_contact(contact, new_contact):
    contact = await select_contact(contact)
    await contact.update(contact=new_contact).apply()
