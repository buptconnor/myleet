__author__ = 'Connor'
# @param A  a list of integers
# @param m  an integer, length of A
# @param B  a list of integers
# @param n  an integer, length of B
# @return nothing
def merge( A, m, B, n):
    A.extend(B)
    print(A )
    if m == 0:
        for i in range(n):
            A[i] = B[i]
    if n == 0:
        return
    i = m - 1
    j = n - 1
    while i >=0 and j >=0:
        if A[i] >= B[j]:
            A[i+j+1] = A[i]
            i -= 1
        else:
            A[i+j+1] = B[j]
            j -= 1
    if i < 0:
        while j >= 0:
            A[j] = B[j]
            j -= 1
    return

aa =[2]#[1,2,3,4]
bb = [1]#[3,5,6,7,8]
merge(aa,len(aa),bb,len(bb))
print(aa)