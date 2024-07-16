"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

def equalPairs(grid):
    grid_hash = {}
    transposed_grid = list(map(list,zip(*grid)))
    # count the occurence of each row in the grid
    for item in grid:
        grid_hash[str(item)] = grid_hash.get(str(item),0)+1


    count = 0
    # Count the occurrence of each column in the transposed grid
    for item in transposed_grid:
        column_key = str(item)
        if column_key in grid_hash:
            count += grid_hash[column_key]
    return count

# def equalPairs(grid):
#     row_hash = {}
#     col_hash = {}
#
#     # count the occurence of each row in the grid
#     for item in grid:
#         row_hash[str(item)] = row_hash.get(str(item),0)+1+1
#
#     for item in list(map(list,zip(*grid))):
#         col_hash[str(item)] = col_hash.get(str(item), 0) + 1
#     # Count the occurrence of each column in the transposed grid
#
#     count = 0
#     for key in row_hash:
#         if key in col_hash:
#             count += row_hash[key] * col_hash[key]
#
#     return count


print(equalPairs([[13,13],[13,13]]))