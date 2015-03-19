__author__ = 'Connor'


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        stack = []
        for i in range(32):
            bit = n & 1
            stack.append(bit)
            n = n>>1
        bb = 0
        for bit in stack:
            bb = bb<<1
            bb = bb | bit

        return bb

if __name__ == '__main__':
    so =Solution()
    aa = 43261596
    ans = so.reverseBits(aa)
    print(ans)