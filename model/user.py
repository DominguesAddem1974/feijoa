from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Table, DateTime, LargeBinary
from sqlalchemy.sql.functions import current_timestamp
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
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def from_dict(obj: dict):
        return User(**{k: v for k, v in obj.items() if k in {'name', 'email'}})

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

    user = User(name='h', email='a')
    user_dict = user.as_dict()
    user_obj = User.from_dict(user_dict)
    # print(user_dict)
    # print(user_obj.__dict__)
