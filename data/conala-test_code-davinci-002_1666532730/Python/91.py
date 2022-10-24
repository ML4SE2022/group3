from datetime import datetime, timedelta

# subtract 100 years
datetime.now() - timedelta(days=365*100)

# add 100 years
datetime.now() + timedelta(days=365*100)