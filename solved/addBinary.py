__author__ = 'Connor'
# @param a, a string
# @param b, a string
# @return a string
def addBinary(a,b):
    if a =='':
        return b
    if b == '':
        return a
    carry = 0
    if len(a) >= len(b):
        long = a
        short = b
        length = len(a)+1
    else:
        long = b
        short = a
        length = len(b)+1

    c = [0 for i in range(length)]
    for i in range(len(short)):
        c[length-1-i] = int(long[length-2-i]) + int(short[len(short)-1-i]) + carry
        if c[length-1-i]>=2:
            carry = 1
            c[length-1-i] -= 2
        else:
            carry = 0
    i += 1
    while i < len(long):
        c[length-1-i] = int(long[length-2-i]) + carry
        if c[length-1-i]>=2:
            carry = 1
            c[length-1-i] -= 2
        else:
            carry = 0
        i += 1
    if carry>0:
        c[0] = carry
    else:
        c.remove(c[0])
    print(c)
    res = ''
    for i in c:
        res+=str(i)
    return res

def test(a,b):
    if a =='':
        return b
    if b == '':
        return a
    carry = 0
    if len(a) >= len(b):
        long = a
        short = b
    else:
        long = b
        short = a
    lenl = len(long)
    lens = len(short)
    res =''
    for i in range(lens):
        tmp =int(long[lenl-1-i])+int( short[lens-1-i]) + carry
        if tmp>=2:
            carry=1
            res  = str(tmp-2) +res
        else:
            carry = 0
            res = str(tmp) +res
    i += 1
    while i < lenl:
        tmp =int(long[lenl-1-i])+ carry
        if tmp>=2:
            carry=1
            res  = str(tmp-2) +res
        else:
            carry = 0
            res = str(tmp) +res
        i +=1
    if carry==0:
        return res
    else:
        return '1'+res




a = '1011'
b = '10'
ans = test(a,b)
print(ans)