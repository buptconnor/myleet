__author__ = 'Connor'
def minPathSum(grid):
    M = len(grid)
    N = len(grid[0])
    Table = [[0 for j in range(N)] for i in range(M)]
    Table[M-1][N-1] = grid[M-1][N-1]
    i =  M - 2
    while i >= 0:
        Table[i][N-1] = Table[i+1][N-1] + grid[i][N-1]
        i -= 1
    j = N - 2
    while j >= 0:
        Table[M-1][j] = Table[M-1][j+1] + grid[M-1][j]
        j -= 1
    i = M-2
    while i >= 0:
        j = N -2
        while j >=0:
            Table[i][j] = min(Table[i+1][j],Table[i][j+1]) + grid[i][j]
            j -= 1
        i -= 1
    return Table[0][0]

aa =[
  [0,2,0],
  [5,1,3],
  [0,2,0]
]

ans =  minPathSum(aa)
print(ans)