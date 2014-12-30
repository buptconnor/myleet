__author__ = 'Connor'
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Follow up:
# Could you do this in-place?
# a[i][j]->b[j][N-1-i]


def rotate(matrix):
    N = len(matrix)
    for i in range(int(N/2)):
        for j in range(N-2*i-1):
            matrix = swap4(matrix,i,i+j)
            #print(matrix)
    return matrix

def swap4(A,i,j):
    N = len(A)
    tmp = A[i][j]

    A[i][j] = A[N-1-j][i]
    A[N-1-j][i] = A[N-1-i][N-1-j]
    A[N-1-i][N-1-j] = A[j][N-1-i]
    A[j][N-1-i] =tmp

    return A

aa = [[0,1,2,3],
      [10,11,12,13],
      [20,21,22,23],
      [30,31,32,33]
]
bb = [[00,1,2],
      [10,11,12],
      [20,21,22]
]
cc = [[0,1],
      [10,11]
]
dd = [[0,1,2,3,4],
      [10,11,12,13,14],
      [20,21,22,23,24],
      [30,31,32,33,34],
      [40,41,42,43,44]

]
ee =[1]
ans = rotate(ee)
print(ans)


