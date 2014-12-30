__author__ = 'Connor'
# @param matrix, a list of lists of integers
# RETURN NOTHING, MODIFY matrix IN PLACE.
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

def setZeroes(matrix):
    if matrix == []:
        return
    M = len(matrix)
    N = len(matrix[0])
    Row0 = []
    Col0 = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                Row0.append(i)
                Col0.append(j)
    for i in Row0:
        matrix[i] = [0 for ii in range(N)]
    for j in Col0:
        for ii in range(M):
            matrix[ii][j] = 0
    return


aa = [
    [0,1,2,3],
    [2,3,41,4],
    [4,3,0,2]
]
setZeroes(aa)
print(aa)