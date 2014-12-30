__author__ = 'Connor'
def searchInsert(A, target):
    if A == []:
        return 0
    if A[0] > target:
        return 0
    if A[len(A)-1] < target:
        return len(A)
    pos = find(A,target,0,len(A)-1)

    return pos
def find(A,target,s,e):
    half = int((s+e)/2)
    if A[s] ==target:
        return s
    elif A[e] == target:
        return e
    elif A[half] == target:
        return half
    elif s == half:
        return e
    if A[s] < target and target < A[half]:
        pos = find(A,target,s,half)
    elif A[half] < target and target < A[e]:
        pos = find(A,target,half,e)
    return pos

aa = [1] #[1,3,5,6]
tt = 4
ans = searchInsert(aa,tt)
print(ans)