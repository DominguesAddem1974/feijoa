import sys,os
sys.path.append(os.getcwd())
import model.user


from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

session = Session(engine, future=True)

user = model.user.User(name='hello', email='hello@world.com')

session.add(user)
session.commit()

a = session.query(model.user.User).all()

print(a)