__author__ = 'Connor'
def jump(A):
    last = 0
    maxlen = 0
    jumps = 0
    for i in range(len(A)):
        if i > last:
            last = maxlen
            jumps += 1
        maxlen = max(maxlen,i+A[i])

    return jumps

aa = [2,3,1,1,4]
print(jump(aa))