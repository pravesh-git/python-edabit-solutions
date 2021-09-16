"""Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.

Examples
get_last_item([1, 2, 3]) ➞ 3

get_last_item(["cat", "dog", "duck"]) ➞ "duck"

get_last_item([True, False, True]) ➞ True

get_last_item([7, "String", False]) ➞ False"""

def get_last_item(lst):
#    return lst[-1]
    list_leg = len(lst)
    last_item = lst[list_leg - 1]
    return last_item

#Another Way:
# return lst[-1]


print(get_last_item([7, "String", False]))
