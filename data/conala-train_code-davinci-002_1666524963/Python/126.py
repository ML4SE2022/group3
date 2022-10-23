import re

def remove_periods_in_acronyms(text):
    return re.sub(r'\b([A-Z]\.)+\b', lambda m: m.group().replace('.', ''), text)