__author__ = 'Connor'
from TreeNode import consturctdefault
from TreeNode import constructBST
from TreeNode import constructSymmeric

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


if __name__ == '__main__':
    tt = consturctdefault()
    tb = constructBST()
    ts = constructSymmeric()
    so = Solution()
    print(so.maxDepth(tt))
    print(so.maxDepth(tb))
    print(so.maxDepth(ts))