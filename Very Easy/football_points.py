"""
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points

Examples
football_points(3, 4, 2) ➞ 13
football_points(5, 0, 2) ➞ 15
football_points(0, 0, 1) ➞ 0
"""

def football_points(x,y,z):
    win = x * 3
    draw = y * 1
    loss = 0

    final_points = win + draw + loss
    return final_points

print(football_points(3, 4, 2))
print(football_points(5, 0, 2))
print(football_points(0, 0, 1))