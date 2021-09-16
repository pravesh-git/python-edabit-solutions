def profitable_gamble(prob, prize, pay):
    return ((prob * prize) - pay) >= 1

print(profitable_gamble(0.2, 50, 9))
print(profitable_gamble(0.9, 1, 2))