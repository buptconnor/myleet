__author__ = 'lenovo'

#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        paths = [[0]]
        i = 1
        while i <len(triangle):
            tmp = []
            while paths != []:
                path = paths.pop()

                lastnode = path[len(path)-1]
                npath = deepcopy(path)
                npath.append(lastnode)
                tmp.append(npath)

                path.append(lastnode + 1)
                tmp.append(path)
            paths = tmp
            i += 1
        min_sum = 2**31 -1
        for p in paths :
            path_sum = 0
            for i in range(len(p)):
                path_sum += triangle[i][p[i]]
            min_sum = min(min_sum,path_sum)
        return min_sum

    def test2(self,triangle):
        dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
        for i in range(len(triangle)):
            if i == 0 :
                dp[i][0] = triangle[0][0]
            if i != 0:
                dp[i][0] = dp[i-1][0] + triangle[i][0]
                dp[i][i] = dp[i-1][i-1] + triangle[i][i]
                for j in range(1,i):
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
        print(dp)
        return min(dp[len(triangle)-1])


    def test(self,triangle):
        return re_minimumTotal(triangle,0,0)

def re_minimumTotal(triangle,i,j):
    if i < len(triangle):
        min_sum = triangle[i][j]
        min_sum += min(re_minimumTotal(triangle,i+1,j),re_minimumTotal(triangle,i+1,j+1))
        return min_sum
    else:
        return 0

def deepcopy(li):
    newli = []
    for i in li:
        newli.append(i)
    return newli

if __name__ == '__main__':
    so =Solution()
    tri =[
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]

    ans = so.test2(tri)
    print(ans)