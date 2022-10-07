from utils.db_api.db_mgotu import TimedBaseModel
from sqlalchemy import *
from sqlalchemy import sql


class Doc(TimedBaseModel):
    __tablename__ = 'documents'

    doc_id = Column(Integer, primary_key=True)
    build = Column(String(30))
    name_file = Column(String(200))
    file_url = Column(String(400))

    query: sql.select