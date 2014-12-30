__author__ = 'Connor'
def plusOne(digits):
    length = len(digits)
    ans = [0 for i in range(length+1)]
    i = length
    carry = 1
    while i > 0:
        ans [i] = digits[i-1] + carry
        if ans[i] >=10:
            carry = 1
            ans[i] -= 10
        else:
            carry = 0
        i -= 1
    if carry == 1:
        ans[0] = carry
    else:
        ans.remove(0)
    return ans

aa= [7]
ans = plusOne(aa)
print(ans)
