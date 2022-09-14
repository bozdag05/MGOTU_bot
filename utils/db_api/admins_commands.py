from utils.db_api.schemas.db_admins import Admin
from utils.db_api.db_mgotu import db
from asyncpg import UniqueViolationError


async def add_admin(admin_id: int, first_name: str, last_name: str, username: str, status: str):
    try:
        admin = Admin(admin_id=admin_id, first_name=first_name, last_name=last_name, username=username, status=status)
        await admin.create()

    except UniqueViolationError:
        print("admin add error")


async def select_all_admins():
    admins = await Admin.query.gino.all()
    return admins


async def count_admins():
    count = await db.func.count(Admin.admin_id).gino.scalar()
    return count


async def select_admin(admin_id):
    admin = await Admin.query.where(Admin.admin_id == admin_id).gino.first()
    return admin


async def delete_admin(admin_id):
    room = await Admin.query.where(Admin.admin_id == admin_id).gino.first()
    await room.delete()


async def update_status(admin_id, new_status):
    admin = await select_admin(admin_id)
    await admin.update(status=new_status).apply()
