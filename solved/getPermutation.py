__author__ = 'Connor'
# @return a string
def getPermutation(n,k):
    Table = [i+1 for i in range(n)]
    res = ''
    tt = k
    i = n
    while i > 0:
        tmp = fac(i-1)
        j = 0
        while tt > j*tmp:
            j += 1
        res += str(Table[j-1])
        Table.remove(Table[j-1])
        tt -= (j-1)*tmp
        i -= 1
    return res
def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)


ans = getPermutation(4, 2)
print(ans)