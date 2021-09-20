def num_to_dashes(n):
    if n in range(1,61):
        return str(n*"-")
    else:
        return "n not in range"

print(num_to_dashes(1))