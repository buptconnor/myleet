__author__ = 'Connor'

from TreeNode import TreeNode
from TreeNode import printTree
from TreeNode import constructdefault1
from TreeNode import constructUnbalanced

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        hl = height(root.left)
        hr = height(root.right)
        return abs(hl -hr) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


def height(root):
    if root == None:
        return 0
    else:
        if root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            return 1 + height(root.right)
        elif root.left != None and root.right == None:
            return 1 + height(root.left)
        else:
            return max(height(root.left),height(root.right))+1



if __name__ == '__main__':
    so = Solution()
    # tt = constructdefault1()
    tb = constructUnbalanced()
    printTree(tb)
    # print(so.isBalanced(tt))
    print(so.isBalanced(tb))
