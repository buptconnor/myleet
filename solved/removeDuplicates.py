__author__ = 'Connor'
def removeDuplicates(A):
    if A == []:
        return 0
    i=1
    num=0
    while i<len(A):
        if A[i]!=A[num]:
            num+=1
            A[num]=A[i]
        i+=1
    j=num+1
    B = A[0:num+1]
    A = B
    # while j<i:
    #     A[j] = None
    #     j+=1
    print(B)
    return num+1

a=[1,1,1,2,3,4,4,4,4,5]
#a=[1,1]
print(removeDuplicates(a))
print(a)