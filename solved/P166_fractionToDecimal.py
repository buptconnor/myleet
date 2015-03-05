__author__ = 'Connor'

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        sign = (0 if numerator*denominator >= 0 else 1)
        nr = abs(numerator)
        dr = abs(denominator)
        p1 = int(nr/dr)
        p2 = int(nr%dr)
        if p2 == 0:
            return str(p1) if sign == 0 else '-'+ str(p1)
        else:
            ans = ''
            res = p2
            resarr = [res]
            while res != 0:
                q = int(res*10/dr)
                ans += str(q)
                res = res*10 % dr
                if res in resarr:
                    index = resarr.index(res)
                    return str(p1)+'.'+ans[0:index]+'('+ans[index:]+')' if sign ==0 else '-'+str(p1)+'.'+ans[0:index]+'('+ans[index:]+')'
                resarr.append(res)
            return str(p1) + '.'+ans if sign == 0 else '-'+str(p1) + '.'+ans

if __name__ == '__main__':
    so =Solution()
    ans = so.fractionToDecimal(-50,8)
    print(ans)
