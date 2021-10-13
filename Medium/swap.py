"""
Create a function that flips M's to W's (all uppercase).

Examples
wumbo("I LOVE MAKING CHALLENGES") ➞ "I LOVE WAKING CHALLENGES"

wumbo("MEET ME IN WARSAW") ➞ "WEET WE IN WARSAW"

wumbo("WUMBOLOGY") ➞ "WUWBOLOGY"
Notes
N/A
"""

import re
def wumbo(str):
    new_str = re.sub("M","W",str)
    return new_str

print(wumbo("WUMBOLOGY"))