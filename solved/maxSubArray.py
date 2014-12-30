__author__ = 'Connor'
def maxSubArray(A):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    maxSum = A[0]
    for i in range(len(A)):
        if A[i]>0:
            maxSum = 0
            break
        else:
            maxSum = max(maxSum,A[i])
    if maxSum != 0:
        return maxSum
    preSum = 0
    while i <len(A):
        if A[i] < 0:
            i += 1
            continue
        k = 1
        if (i +k) < len(A)-1 and A[i+k]>=0:
            preSum += A[i]
            i +=1
            continue
        sumup =preSum + A[i]
        while (i+k)<(len(A)-1) and A[i+k]<0:
            sumup += A[i+k]
            k +=1
        if sumup < 0 or (i+k)>=len(A):
            maxSum = max(maxSum,preSum +A[i])
            preSum = 0
        else:
            maxSum = max(maxSum,preSum +A[i])
            preSum = sumup
        i += k
    maxSum = max(maxSum,preSum)
    return maxSum

aa = [-2,1,-3,4,-1,2,1,-5,4]
# aa = [-2,-1]
#aa = [1,2,-1,-2,2,1,-2,1,4,-5,4]
aa = [2,0,-3,2,1,0,1,-2]
ans =maxSubArray(aa)
print(ans)
