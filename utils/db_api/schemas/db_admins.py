from utils.db_api.db_mgotu import TimedBaseModel
from sqlalchemy import String, Column, sql, BigInteger


class Admin(TimedBaseModel):
    __tablename__ = 'admins'

    admin_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(200))
    status = Column(String(50))

    query: sql.select
