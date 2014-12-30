__author__ = 'Connor'
# @param x, a float
    # @param n, a integer
    # @return a float
def pow(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n >= 0:
        sign = 0
    else:
        sign = 1
    n = abs(n)
    tmp = pow(x,int(n/2))
    if n % 2 ==1:
        res = tmp*tmp*x
    else:
        res = tmp*tmp
    if sign == 1:
        return 1/res
    return res

print(pow(2,3))