s = '\u00e9'
s
'é'
s.encode('utf-8')
b'\xc3\xa9'
s.encode('utf-8').decode('utf-8')
'é'