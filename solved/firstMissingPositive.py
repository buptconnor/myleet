__author__ = 'Connor'
def firstMissingPositive(A):

    if A == []:
        return 1
    i = 0
    length = len(A)
    while i <length:
       if A[i]>0 and A[i]<length and A[i] != A[A[i]-1]:
            A = swap(A,i,A[i]-1)
       else:
           i += 1
    i = 0
    for i in range(length):
        if A[i]!= i+1:
            return i+1
    return length+1


def swap(A,i,j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    return A

if __name__ =='__main__':
    # ans = mytest(26)
    # print(ans)
    aa = [39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]
    bb = [3,4,-1,0,1,7]

    ans = firstMissingPositive(bb)
    print(ans)