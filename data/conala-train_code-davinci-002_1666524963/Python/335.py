import re

def remove_between(text, begin, end):
    return re.sub(r'{}.*?{}'.format(begin, end), '', text)

remove_between('abc123def456ghi789', '123', '789')