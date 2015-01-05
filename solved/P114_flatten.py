__author__ = 'Connor'

from TreeNode import contstructFlatten
from TreeNode import printTree

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return
        elif root.left == None and root.right != None:
            self.flatten(root.right)
            return
        elif root.left != None and root.right == None:
            root.right = root.left
            root.left = None
            self.flatten(root.right)
            return
        else:
            tmp = root.right
            self.flatten(tmp)
            root.right = root.left
            root.left = None
            self.flatten(root.right)
            p = root.right
            while p.right != None:
                p = p.right
            p.right = tmp
            return

        # p = root
        # tmp = p.right
        # p.right = p.left
        # self.flatten(p.left)
        # q = p.left
        # while q.right != None:
        #     q = q.right
        # q.right = tmp
        # return

def isLeaf(root):
    return root.left == None and root.right == None

if __name__ == '__main__':
    so = Solution()
    tf = contstructFlatten()
    so.flatten(tf)
    printTree(tf)