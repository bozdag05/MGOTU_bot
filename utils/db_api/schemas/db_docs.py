from utils.db_api.db_mgotu import TimedBaseModel
from sqlalchemy import *
from sqlalchemy import sql


class Doc(TimedBaseModel):
    __tablename__ = 'documents'

    build = Column(String(30))
    name_file = Column(String(200), primary_key=True)
    file_url = Column(String(400))

    query: sql.select