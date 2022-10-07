from sqlalchemy import *
from sqlalchemy import sql
from utils.db_api.db_mgotu import TimedBaseModel


class Room(TimedBaseModel):
    __tablename__ = 'rooms'

    room_id = Column(Integer, primary_key=True)
    number = Column(String(10))
    build = Column(String(30))
    title = Column(String(200))
    comment = Column(String(2000))
    nomer = Column(String(15))

    query: sql.select
