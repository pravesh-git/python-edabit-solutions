#calculator("13+2-5*2") ➞ 5
#Use eval() builtin function from python

def calculator(user_string):
    return eval(user_string)

print(calculator("13+2-5*2"))