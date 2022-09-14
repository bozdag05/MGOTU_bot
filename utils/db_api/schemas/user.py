from sqlalchemy import sql, Column, String, BigInteger
from utils.db_api.db_mgotu import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(200))
    status = Column(String(30))

    query: sql.select
