__author__ = 'Connor'
def uniquePaths(m,n):
    if m ==1 or n ==1:
        return 1
    return uniquePaths(m-1,n) + uniquePaths(m,n-1)

def uniquePaths2(m,n):
    Table = [[0 for j in range(m)] for i in range(n)]
    # print(Table)
    for i in range(m):
        Table[n-1][i] = 1
    for j in range(n):
        Table[j][m-1] = 1
    i = n-2
    while i >= 0:
        j = m-2
        while j >= 0:
            Table[i][j] = Table[i+1][j] + Table[i][j+1]
            j -= 1
        i -= 1
    # Table[0][0] = Table[0][1] +Table[1][0]
    return Table[0][0]

# print(uniquePaths(7,3))
print(uniquePaths2(7,3))




