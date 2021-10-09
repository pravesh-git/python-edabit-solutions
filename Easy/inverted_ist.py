def invert_list(lst):
    inv_list = []
    for i in lst:
        inv_list.append(-i)
    return inv_list

#return [-i for i in lst]

print(invert_list([1,2]))

