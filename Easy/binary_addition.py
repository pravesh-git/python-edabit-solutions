#num = 11
#print(bin(num))

"""
Create a function that takes two numbers and returns their sum as a binary string.

Examples
add_binary(1, 1) ➞ "10"

add_binary(1, 2) ➞ "11"

add_binary(4, 5) ➞ "1001"
Notes
Remember to return the converted result to a string.
Check the resources tab in case you are stuck :)
"""

def add_binary(n,m):
    return bin(n+m)[2:]

print(add_binary(4, 5))