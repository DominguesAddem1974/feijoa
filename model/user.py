from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Table, DateTime, BLOB
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable
import sqlalchemy
print('--', sqlalchemy.__version__)

# declarative base class
Base = declarative_base()

# an example mapping using the base
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

if __name__ == '__main__':
    print(CreateTable(User.__table__).compile(dialect=postgresql.dialect()))
