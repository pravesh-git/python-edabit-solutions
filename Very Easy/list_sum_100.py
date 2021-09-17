"""
Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.
"""

def list_less_than_100(lst):
    return (sum(lst) < 100)

print(list_less_than_100([5, 57]))