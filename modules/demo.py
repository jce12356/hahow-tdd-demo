from . import Base
from datetime import datetime
from sqlalchemy import string, DATETIME, INTEGER, Column


class DemoUser(Base):
    __tablename__ = "demo_user"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String(64))
    birthday = Column(DATETIME)