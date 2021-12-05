from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Table, DateTime, LargeBinary
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

#engine = sqlalchemy.create_engine("postgres://postgres:postgres@localhost/postgres",
                    #    echo=True,
                    #    pool_size=8,
                    #    pool_recycle=60*30
                    #    )
#Base.metadata.create_all(engine)

if __name__ == '__main__':
    print(CreateTable(User.__table__).compile(dialect=postgresql.dialect()), end=';\n')
    init_sql = [
        "CREATE USER readonly WITH PASSWORD 'readonly';",
        "GRANT SELECT ON public.user TO readonly;",
    ]
    for s in init_sql:
        print(s)

