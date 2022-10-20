from pycassa.system_manager import *

sys = SystemManager('127.0.0.1:9160')

# Get the keyspace
ks = sys.get_keyspace('Keyspace1')

# Get the column family
cf = ks.get_column_family('Standard1')

# Get all the keys
for key in cf.get_range():
    print key