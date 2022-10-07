from utils.db_api.schemas.db_rooms import Room
from utils.db_api.db_mgotu import db
from asyncpg import UniqueViolationError


async def add_room(room_id: int, build: str,  number: str, title: str, comment: str, nomer):
    try:
        room = Room(room_id=room_id, build=build, number=number, title=title, comment=comment, nomer=nomer)
        await room.create()

    except UniqueViolationError:
        print(" add room error")


async def select_all_rooms():
    rooms = await Room.query.gino.all()
    return rooms


async def count_room():
    count = await db.func.count(Room.room_id).gino.scalar()
    return count


async def select_room_id(room_id):
    room = await Room.query.where(Room.room_id == room_id).gino.first()
    return room


async def select_room(number):
    room = await Room.query.where(Room.number == number).gino.first()
    return room


async def delete_room(room_id):
    room = await Room.query.where(Room.room_id == room_id).gino.first()
    await room.delete()


async def select_rooms(build):
    rooms = await Room.query.where(Room.build == build).gino.all()
    return rooms


async def update_room(number, new_build, new_title, new_comment, new_nomer):
    room = await select_room(number)
    await room.update(build=new_build, title=new_title, comment=new_comment, nomer=new_nomer).apply()
