#!/usr/bin/env python

import re

def find_dict_items(d, substr):
    """
    Find dictionary items whose key matches a substring.
    """
    return {k: v for k, v in d.items() if re.search(substr, k)}

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print(find_dict_items(d, 'a'))
    print(find_dict_items(d, 'b'))
    print(find_dict_items(d, 'c'))
    print(find_dict_items(d, 'd'))
    print(find_dict_items(d, 'e'))
    print(find_dict_items(d, 'f'))
```

```shell
$ ./find_dict_items.py
{'a': 1}
{'b': 2}
{'c': 3}
{'d': 4}
{'e': 5}
{}