__author__ = 'Connor'
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

def generateMatrix(n):
    if n <= 0:
        return []

    ans = [[0 for i in range(n)] for i in range(n)]
    num = 1
    for i in range(int((n+1)/2)):
        if n-2*i == 1:
            ans[i][i]=num
        for j in range(n-2*i-1):
            ans[i][i+j] =num
            num += 1
        for j in range(n-2*i-1):
            ans[i+j][n-i-1] =num
            num += 1
        for j in range(n-2*i-1):
            ans[n-i-1][n-i-1-j] =num
            num += 1
        for j in range(n-2*i-1):
            ans[n-i-1-j][i] =num
            num += 1
    return ans


ans = generateMatrix(6)
print(ans)