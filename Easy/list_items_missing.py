"""
Create a function that returns a list of all the integers between two given numbers start and end.

Examples
range_of_num(2, 4) ➞ [3]

range_of_num(5, 9) ➞ [6, 7, 8]

range_of_num(2, 11) ➞ [3, 4, 5, 6, 7, 8, 9, 10]
Notes
start will always be <= end.
start and end are NOT included in the final list.
If start == end, return an empty list.
"""

def range_of_num(x,y):
    missinglist=[]
    if x==y:
        return missinglist
    else:
        return list(range(x+1,y))


print(range_of_num(5, 9))
