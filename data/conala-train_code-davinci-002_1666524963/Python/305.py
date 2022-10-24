# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

# Use the .execute() method on the engine to execute a statement and store the results
results = engine.execute('SELECT * FROM state_fact')

# Use the .fetchall() method on the results to get a list of the results
print(results.fetchall())

# Use the .first() method on the results to get the first row of the results
print(results.first())

# Get the number of rows in the results using the .rowcount() method
print(results.rowcount)