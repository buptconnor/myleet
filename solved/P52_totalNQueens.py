__author__ = 'Connor'

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        ans = 0
        queens = [-1 for i in range(n)]
        i = j =0
        while i < n:
            while j < n:
                if valid(queens,i,j,n):
                    queens[i] = j
                    j = 0
                    break
                else:
                    j += 1
            if queens[i] == -1:
                if i == 0 :
                    break
                else:
                    i -= 1
                    j = queens[i] +1
                    queens[i] = -1
                    continue
            if i == n-1:
                ans += 1
                j = queens[i] + 1
                queens[i] = -1
                continue
            i += 1
        return ans

def valid(queens,row,col,n):
    for i in range(row):
        if (col == queens[i]) or (abs(i - row) == abs(queens[i] - col)):
            return False
    return True

if __name__ == '__main__':
    so = Solution()
    print(so.totalNQueens(4))
