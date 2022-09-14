from sqlalchemy import *
from sqlalchemy import sql
from utils.db_api.db_mgotu import TimedBaseModel


class Room(TimedBaseModel):
    __tablename__ = 'rooms'

    number = Column(String(10), primary_key=True)
    build = Column(String(30))
    title = Column(String(200))
    comment = Column(String(2000))
    nomer = Column(BIGINT)

    query: sql.select
