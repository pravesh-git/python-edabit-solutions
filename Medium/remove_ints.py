def remove_numbers(string):
    return "".join(i for i in string if i.isalpha())

print(remove_numbers("mubashir1"))