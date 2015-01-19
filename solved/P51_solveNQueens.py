__author__ = 'Connor'
# 4-Q problem:
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

def solveNQueens(n):
    # if n ==1:
    #     return [['Q']]
    ans = []
    queens = [-1 for i in range(n)]
    i = j = 0
    while i < n:
        while j < n:
            if valid(queens,i,j,n):
                queens[i] = j
                j = 0
                break
            else:
                j += 1
        if queens[i] == -1:
            if i ==0 :
                break;
            else:
                i -= 1
                j = queens[i] +1
                queens[i] = -1
                continue
        if i == n - 1:

            ans.append(convert(queens))
            j = queens[i] + 1
            queens[i] = -1
            continue
        i += 1
    return ans

def convert(queens):
    ans =[]

    for i in range(len(queens)):
        tmp = ''
        j = 0
        while j < queens[i]:
            tmp += '.'
            j += 1
        tmp += 'Q'
        j += 1
        while j < len(queens):
            tmp += '.'
            j += 1
        ans.append(tmp)
    return ans

def valid(queens,row,col,n):
    for i in range(row):
        if (queens[i] == col) or (abs(i-row) == abs(queens[i]-col)):
            return False
    return True


ans = solveNQueens(1)
print(ans)