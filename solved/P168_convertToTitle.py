__author__ = 'Connor'
def convertToTitle(num):
    dic = [chr(ord('A')+i) for i in range(26)]
    print(dic)
    k = num
    ans = ''
    # if num<=26:
    #     return dic[k-1]
    while k>0:
        tmp =int(k%26)
        k = int(k/26)
        if tmp == 0:
            k -= 1
        ans = dic[tmp-1] +ans
    return ans

ans = convertToTitle(27)
print(ans)