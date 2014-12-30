__author__ = 'Connor'
def divide( dividend, divisor):
    ans = 0
    sign1 = dividend >= 0
    sign2 = divisor >= 0
    if (sign1 and sign2) or (not sign1 and not sign2):
        sign = True
    else :
        sign = False
    #sign = sign1 and sign2
    d1 =abs(dividend)
    d2 = abs(divisor)
    if d1>=d2:
        ans+=1
    while d1-d2>=d2:
        d2+=d2
        ans+=ans
    d1-=d2

    while d1-abs(divisor) >= 0:
        d1-=abs(divisor)
        ans+=1

    if sign:
        return ans
    else:
        return -ans

print(divide(6,-6))