__author__ = 'Connor'
# @param obstacleGrid, a list of lists of integers
# @return an integer

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    Table = [[0 for j in range(n)] for i in range(m)]
    i = m-2
    if obstacleGrid[m-1][n-1] == 1:
        return 0
    Table[m-1][n-1] = 1
    while i >= 0:
        if obstacleGrid[i][n-1] == 1 or Table[i+1][n-1] == 0:
            Table[i][n-1] =0
        else:
            Table[i][n-1] = 1
        i -= 1
    i = n - 2
    while i >= 0 :
        if obstacleGrid[m-1][i] == 1 or Table[m-1][i+1] ==0:
            Table[m-1][i] = 0
        else:
            Table[m-1][i] = 1
        i -= 1
    i = m-2
    while i >= 0:
        j = n-2
        while j >= 0:
            if obstacleGrid[i][j] == 1:
                Table[i][j] = 0
            else:
                Table[i][j] = Table[i+1][j]+Table[i][j+1]
            j-=1
        i-=1
    return Table[0][0]


aa =[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

ans = uniquePathsWithObstacles(aa)
print(ans)