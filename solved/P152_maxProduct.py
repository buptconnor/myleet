__author__ = 'Connor'

# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return A[0]
        i = 0
        max_product = 0
        tmp = 1
        poz = -1 # position of zero
        pon = -1 # position of negative
        non = 0  # number of negative since last 0
        while i < len(A):
            if A[i] > 0:
                tmp *= A[i]
                max_product = max(max_product,tmp)
            elif A[i] == 0:
                tmp = 1
                non = 0
            else:
                tmp = 1
                if non == 0:
                    pon = i
                    non += 1
                else:
                    non += 1
                    if non%2 == 0:
                        j = i
                        product = 1
                        while j >= pon:
                            product *= A[j]
                            j -= 1
                        max_product = max(max_product,product)
                        tmp = product
                    else:
                        j = i
                        product = 1
                        while j > pon:
                            product *= A[j]
                            j -= 1
                        max_product = max(max_product,product)
                        tmp = product
            i += 1


        return max_product

    def maxProduct1(self,A):
        if len(A) == 1:
            return A[0]
        max_all = A[0]
        localmax = A[0]
        localmin = A[0]
        i = 1
        while i < len(A):
            tmp = localmax
            localmax,localmin = max(A[i],A[i] * localmax, A[i] * localmin),min(A[i],A[i] * tmp, A[i] * localmin)
            max_all = max(localmax,max_all)
            i += 1
        return max_all
if __name__ == '__main__':
    so =Solution()
    aa = [2,3,-2,4,0,-1,-2,5,-3,2,-2,0,2,3,-2]
    ans = so.maxProduct1(aa)
    print(ans)