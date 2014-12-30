__author__ = 'Connor'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import constructSymmeric
from TreeNode import consturctdefault

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            if root.left == None and root.right == None:
                return True
            elif (root.left != None and root.right == None) or (root.left == None and root.right != None):
                return False
            else:
                return compare(root.left, root.right)

def compare(p,q):
    sp = NodeStructure(p)
    sq = NodeStructure(q)
    if sp == sq :
        if sp == 0:
            return p.val == q.val
        if sp == 1:
            return p.val == q.val and compare(p.left, q.right) and compare(p.right, q.left)
        else:
            return False
    else:
        if sp == 2 and sq == 3:
            return p.val == q.val and compare(p.right, q.left)
        if sp == 3 and sq == 2:
            return p.val == q.val and compare(p.left, q.right)
        else:
            return False

def NodeStructure(p):
    if p.left != None and p.right != None:
        return 1
    elif p.left == None and p.right != None:
        return 2
    elif p.left!= None and p.right == None:
        return 3
    elif p.left == None and p.right == None:
        return 0


if __name__ == '__main__':
    st = constructSymmeric()
    tt = consturctdefault()
    so = Solution()
    ans = so.isSymmetric(st)
    print(ans)
    print(so.isSymmetric(tt))

