__author__ = 'Connor'

from TreeNode1 import consturctdefault
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        p = root
        while p != None and  p.left == None and p.right == None:
            p = p.next
        if p != None:
            lastchild = None
            while p != None:
                if p.left != None and p.right != None:
                    p.left.next = p.right
                    lastchild = p.right
                if p.left == None and p.right != None:
                    lastchild = p.right
                if p.left != None and p.right == None:
                    lastchild = p.left
                firstchild = None
                if p.next != None:
                    q = p.next
                    while firstchild == None and q != None:
                        firstchild = (q.left if q.left != None else q.right)
                        q = q.next
                lastchild.next = firstchild
                p = p.next
            m = root
            nextfirst = None
            while nextfirst == None and m != None:
                nextfirst = (m.left if m.left != None else m.right)
                m = m.next
            self.connect(nextfirst)
        return


if __name__ == '__main__':
    tt = consturctdefault()
    so = Solution()
    so.connect(tt)
    print('hello')