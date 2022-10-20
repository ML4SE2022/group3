from sqlalchemy import select, insert

# Create a table
metadata = MetaData()
table = Table('t1', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)))

# Create an insert statement for the table
stmt = insert(table)

# Create a select statement for the table
select_stmt = select([table])

# Create an insert statement which includes a select
stmt = insert(table).from_select(['id', 'name'], select_stmt)