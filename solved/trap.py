__author__ = 'Connor'
def trap(A):
    if len(A)<2:
        return 0
    i = 0
    s = 0
    total = 0
    water = 0
    while i<len(A):
        if A[i] < A[s]:
            water +=A[s] - A[i]
        else:
            total += water
            s = i
            water =0
        i += 1
    j = i-1
    e = i-1
    water = 0
    while j > s:
        if A[j]<A[e]:
            water += A[e] - A[j]
        else:
            total += water
            e = j
            water =0
        j -= 1
    total += water
    return total

aa = [5,4,1,2]#[0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(aa)
print(ans)