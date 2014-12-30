__author__ = 'Connor'
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    cnt = [0 for i in range(n)]
    cnt[0]=1
    cnt[1] =2
    i = 2
    while i < n:
        cnt[i] = cnt[i-1] + cnt[i-2]
        i += 1

    return cnt[n-1]

print(climbStairs(3))