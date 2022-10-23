def coalesce(column, default):
    return case([(column != None, column)], else_=default)