__author__ = 'Connor'
# duplicates are allowed at most twice?
# Given sorted array A = [1,1,1,2,2,3],
# Your function should return length = 5, and A is now [1,1,2,2,3].
def removeDuplicates(A):
    if A ==[]:
        return 0
    curNum = A[0]
    cnt = 1
    i = 1
    last = 1
    while i < len(A):
        if A[i] != curNum:
            curNum = A[i]
            cnt = 1
        else:
            cnt += 1
            if cnt > 2:
                i += 1
                continue
        A[last] = curNum
        last += 1
        i += 1
    tmp = len(A)-last
    for i in range(tmp):
        A.pop()
    return last

A = [1,1,1,1,1,2,2,3,3]
ans = removeDuplicates(A)
print(ans)
print(A)