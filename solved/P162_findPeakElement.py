__author__ = 'Connor'
# find a peak element and return its index.
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        p = 0
        i = 1
        while i < len(num):
            if num[i] > num[p]:
                p += 1
            else:
                return p
            i += 1
        return p


if __name__ == '__main__':
    so =Solution()
    aa = [1, 2, 3, 4]
    ans = so.findPeakElement(aa)
    print(ans)