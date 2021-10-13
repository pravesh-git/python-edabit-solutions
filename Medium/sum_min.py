"""
Create a function that takes a 2D list lst returns the sum of the minimum value in each row.

Examples
sum_minimums([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100]
] ➞ 26

# minimum value of the first row is 1
# minimum value of the second row is 5
# minimum value of the third row is 20
"""

def sum_minimums(lst):
    final_list = []
    for i in lst:
        final_list.append(min(i))
    return sum(final_list)

print(sum_minimums([[1, 2, 3, 4, 5],[5, 6, 7, 8, 9],[20, 21, 34, 56, 100]]))