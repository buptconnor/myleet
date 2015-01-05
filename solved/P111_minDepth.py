__author__ = 'Connor'

from TreeNode import constructUnbalanced

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        hl = self.minDepth(root.left)
        hr = self.minDepth(root.right)
        if hl*hr != 0:
            return min(hl,hr)+1
        elif hl == 0:
            return hr + 1
        elif hr == 0:
            return hl + 1



if __name__ == '__main__':
    so = Solution()
    tb = constructUnbalanced()
    print(so.minDepth(tb))