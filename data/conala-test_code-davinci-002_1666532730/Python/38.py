from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)

metadata.create_all(engine)

ins = users.insert()
print(ins)

ins = users.insert().values(name='jack', fullname='Jack Jones')
print(ins)

ins = users.insert()
new_user = ins.values(name='jack', fullname='Jack Jones')
print(new_user)

conn = engine.connect()
result = conn.execute(new_user)
print(result.inserted_primary_key)

ins = users.insert()
result = conn.execute(ins, id=2, name='wendy', fullname='Wendy Williams')
print(result.inserted_primary_key)

conn.close()

ins = users.insert()
conn = engine.connect()
result = conn.execute(ins, [
    {'name': 'jack', 'fullname': 'Jack Jones'},
    {'name': 'wendy', 'fullname': 'Wendy Williams'},
    {'name': 'mary', 'fullname': 'Mary Contrary'},
    {'name': 'fred', 'fullname': 'Fred Flinstone'},
])
print(result.inserted_primary_key)

conn.close()

ins = users.insert()
conn = engine.connect()
result = conn.execute(