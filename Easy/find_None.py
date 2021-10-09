from typing import List


def find_none(lst):
    if None in lst:
        return lst.index(None)
    else:
        return -1 

print(find_none([1, 2, None]))