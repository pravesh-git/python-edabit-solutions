"""
Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

Examples
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720
"""

def sum_polygon(sides):
    if int(sides) <= 2:
        print("Cannot calculate internal angles")
    else:
        return (sides - 2) * 180

print(sum_polygon(3))
print(sum_polygon(4))
print(sum_polygon(6))
print(sum_polygon(1))
print(sum_polygon(2))