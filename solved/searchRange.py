__author__ = 'Connor'
def searchRange(A, target):
    if A == [] :
        return [-1,-1]
    res = searchin(A,target,0,len(A)-1)
    if res == -1:
        return [-1,-1]
    ss = res
    ee = res
    while ss-1 > 0 and A[ss-1] == target:
        ss -=1
    while ee+1 <len(A) and A[ee+1] == target:
        ee +=1
    return [ss,ee]

def searchin(A,t,s,e):
    half =int((s+e)/2)
    if A[s] ==t:
        return s
    elif A[e] == t:
        return e
    elif A[half] == t:
        return half
    elif s == half:
        return -1
    if A[s] < t and t < A[half]:
        ans = searchin(A,t,s,half)
    elif A[half] < t and t < A[e]:
         ans =searchin(A,t,half,e)
    else:
        return -1
    return ans



aa = [1,2,3,55]#[5, 7, 7, 8, 8, 10]
tt = 2
ans = searchRange(aa,tt)
print(ans)