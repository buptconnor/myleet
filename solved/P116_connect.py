__author__ = 'Connor'

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
        if root == None or root.left == None:
            return
        p = root
        while p != None:
            p.left.next = p.right
            if p.next != None:
                p.right.next=p.next.left
            p = p.next
        self.connect(root.left)
        return
