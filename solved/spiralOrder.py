__author__ = 'Connor'
def spiralOrder(matrix):
    ans = []
    M = len(matrix)
    N = len(matrix[0])
    for i in range(int(len(matrix)/2)+1):
        m = len(matrix)-2*i-1
        if dim ==0:
            ans.append(matrix[i][i])
            break
        for j in range(dim):
            ans.append(matrix[i][i+j])
        for j in range(dim):
            ans.append(matrix[i+j][len(matrix)-i-1])
        for j in range(dim):
            ans.append(matrix[len(matrix)-i-1][len(matrix)-i -1-j])
        for j in range(dim):
            ans.append(matrix[len(matrix)-i-1-j][i])
    return ans


def test(matrix):
    ans = []
    if matrix == []:
        return []
    M = len(matrix)
    N = len(matrix[0])
    for i in range(int(M/2)+1):
        col = M -2*i-1
        row = N -2*i-1
        if col < 0 or row<0:
            break
        if col == 0:
            for j in range(row+1):
                ans.append(matrix[i][i+j])
            break
        if row == 0:
            for j in range(col+1):
                ans.append(matrix[i+j][i])
            break

        for j in range(row):
            ans.append(matrix[i][i+j])
        for j in range(col):
            ans.append(matrix[i+j][N-i-1])
        for j in range(row):
            ans.append(matrix[M-i-1][N-i-1-j])
        for j in range(col):
            ans.append(matrix[M-i-1-j][i])
    return ans





aa = [
 [ 1, 2 ],
 [ 4, 5 ],
 [ 7, 8 ]
]
aa =[
    [ 1, 2, 3, 4, 5],
    [ 6, 7, 8, 9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
# aa=[
#     [ 1, 2, 3, 4],
#     [ 5, 6, 7, 8],
#     [ 9,10,11,12],
#     [13,14,15,16]
# ]
# aa = [
#     [1,2,3],
#     [4,5,6]
# ]
aa =[[1,11],
     [2,12],
     [3,13],
     [4,14],
     [5,15],
     [6,16],
     [7,17],
     [8,18],
     [9,19],
     [10,20]]
ans = test(aa)
print(ans)