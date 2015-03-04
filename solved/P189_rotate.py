__author__ = 'Connor'

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        nn = len(nums)
        # tmp = [nums[(i+k)%nn] for i in range(len(nums))]
        # print(tmp)
        # nums.clear()
        # nums.extend(tmp)
        k1 = k%nn
        stack = nums[nn-k1:]
        i = nn-1
        while i >=k1:
            nums[i] = nums[i-k1]
            i -= 1
        while i >= 0:
            nums[i] = stack[i]
            i -= 1

        return

if __name__ == '__main__':
    so = Solution()
    aa = [1,2,3,4,5,6,7]
    print(aa)
    so.rotate(aa,1)
    print(aa)

