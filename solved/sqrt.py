__author__ = 'Connor'
def sqrt(x):
    if x == 0:
        return 0
    left = 0
    right = int(x/2 + 1)
    while left < right:
        mid =((left + right)/2)
        if mid ** 2<= x < (mid+1) ** 2:
            return int(mid)
        elif x<mid **2:
            right = mid-1
        else:
            left = mid+1

print(sqrt(10100))