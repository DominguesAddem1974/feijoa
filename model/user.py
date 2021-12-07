from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Table, DateTime, LargeBinary, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable
import sqlalchemy
import datetime
import time
from datetime import date
print('--', sqlalchemy.__version__)

# declarative base class
Base = declarative_base()

# an example mapping using the base


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    time_stamp = Column(DateTime, default=current_timestamp())

    def __init__(self, name, email, time_stamp=datetime.datetime.now()):
        self.name = name
        self.email = email
        self.time_stamp = time_stamp

    def as_dict(self):
        user_dict = {c.name: getattr(self, c.name)
                     for c in (self.__table__.columns)}
        user_dict['time_stamp'] = self.time_stamp.timestamp()

        return user_dict

    @staticmethod
    def from_dict(obj: dict):
        user_obj = User(**{k: v for k, v in obj.items()
                        if k in {'name', 'email', 'time_stamp'}})
        #user_obj.time_stamp = datetime.datetime.fromtimestamp(user_obj.time_stamp)
        user_obj.time_stamp = datetime.datetime.utcfromtimestamp(
            user_obj.time_stamp)

        return user_obj

# engine = sqlalchemy.create_engine("postgres://postgres:postgres@localhost/postgres",
        #    echo=True,
        #    pool_size=8,
        #    pool_recycle=60*30
        #    )
# Base.metadata.create_all(engine)


if __name__ == '__main__':
    print(CreateTable(User.__table__).compile(
        dialect=postgresql.dialect()), end=';\n')
    init_sql = [
        "CREATE USER readonly WITH PASSWORD 'readonly';",
        "GRANT SELECT ON public.user TO readonly;",
    ]
    for s in init_sql:
        print(s)
    # print(time.time())
    # print(datetime.datetime.fromtimestamp(time.time()))
    # user = User(name='h', email='a')
    # user_dict = user.as_dict()
    # user_obj = User.from_dict(user_dict)
    # print(user_dict)
    # print(user_obj.__dict__)
    # print(user_obj.time_stamp)
