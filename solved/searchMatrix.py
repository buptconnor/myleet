__author__ = 'Connor'
# @param matrix, a list of lists of integers
# @param target, an integer
# @return a boolean
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
def searchMatrix(matrix, target):
    if matrix == []:
        return False
    M = len(matrix)
    N = len(matrix[0])
    if target<matrix[0][0] or target> matrix[M-1][N-1]:
        return False
    for i in range(M):
        if target > matrix[i][0]:
            if i+1>=M:
                break
            elif target<matrix[i+1][0]:
                break
        else:
            break
    j = 0
    while j<N:
        if target == matrix[i][j]:
            return True
        elif target >matrix[i][j]:
            j += 1
        else:
            break
    return  False

aa =[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

ans = searchMatrix(aa,11)
print(ans)