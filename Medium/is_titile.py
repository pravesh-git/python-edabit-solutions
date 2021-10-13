"""
Check if a string txt is a title text or not. A title text is one which has all the words in the text start with an upper case letter.

Examples
check_title("A Mind Boggling Achievement") ➞ True

check_title("A Simple Python Program!") ➞ True

de("Water is transparent") ➞ False
"""

def check_title(str):
    return str.istitle()

print(check_title("A Simple Python Program!"))
print(check_title("Water is transparent"))