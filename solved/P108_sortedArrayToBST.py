__author__ = 'Connor'

from TreeNode import TreeNode
from TreeNode import preOrder

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num == []:
            return None
        size = len(num)
        locate_root = int(size/2)
        root = TreeNode(num[locate_root])
        root.left = self.sortedArrayToBST(num[:locate_root])
        root.right = self.sortedArrayToBST(num[locate_root+1:])
        return root

if __name__ == '__main__':
    so = Solution()
    aa =[1,2,3,4,5]
    tt = so.sortedArrayToBST(aa)
    preOrder(tt)