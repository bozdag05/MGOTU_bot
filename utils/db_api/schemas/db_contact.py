from sqlalchemy import *
from sqlalchemy import sql
from utils.db_api.db_mgotu import TimedBaseModel


class Contact(TimedBaseModel):
    __tablename__ = 'contacts'

    build = Column(String(30))
    name_men = Column(String(200))
    position = Column(String(200))
    contact = Column(String(15), primary_key=True)

    query: sql.select