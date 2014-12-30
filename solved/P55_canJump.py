__author__ = 'Connor'
def canJump(A):
    can = jumptest(A,0)
    return can
def jumptest(A,index):
    if A[index]+index >= len(A)-1:
        return True
    if A[index] == 0 and index != len(A)-1:
        return False
    i = A[index]
    can = False
    while i> 0:
        res = jumptest(A,index+i)
        can = can or res
        if can:
            return can
        i -= 1
    return can

def test(A):
    if len(A) <=1 or A[0] > len(A)-1:
        return True
    ans = [False for i in range(len(A))]
    i = len(A) - 1
    ans [i] = True
    while i >= 0:
        if A[i] == 0 and i != len(A)-1:
            ans[i] = False
        else:
            j = 0
            while j <= A[i]:
                ans[i] = ans [i] or ans[i+j]
                j += 1
        i -= 1
    return ans[0]

def test2(A):
    if len(A) <=1 or A[0] > len(A)-1:
        return True
    maxjump = A[0]
    if maxjump == 0:
        return False
    for i in range(len(A)):
        if maxjump >= i and i+A[i] >= len(A)-1:
            return True
        if A[i] == 0 and maxjump <= i:
            return False
        if i+A[i]>maxjump:
            maxjump=i+A[i]
    return False
aa1 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]#
aa2= [2,2,0,2,0,4]
#ans = canJump(aa)
ans =test2(aa1)
print(ans)