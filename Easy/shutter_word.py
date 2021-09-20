"""
Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"
Notes
Assume all input is in lower case and at least two characters long.
"""

def stutter(word):
    first_2 = word[0:2]
    return "{}... {}... {}?".format(first_2,first_2,word)


print(stutter("incredible"))
print(stutter("enthusiastic"))