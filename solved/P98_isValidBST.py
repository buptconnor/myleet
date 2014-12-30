__author__ = 'Connor'
from TreeNode import TreeNode
from TreeNode import constructBST
from TreeNode import printTree
import sys

def isValidBST(root):
    if root == None:
        return True
    return isSubTreeLess(root.left,root.val) and isSubTreeGreater(root.right,root.val) and isValidBST(root.left) and isValidBST(root.right)

def isSubTreeLess(root,val):
    if root == None:
        return True
    return root.val<val and isSubTreeLess(root.left,val) and isSubTreeLess(root.right,val)

def isSubTreeGreater(root,val):
    if root == None:
        return True
    return root.val>val and isSubTreeLess(root.left,val) and isSubTreeGreater(root.right,val)

def isValidBST2(root):
    if root == None:
        return True
    return rec(root,-sys.maxsize-1,sys.maxsize)

def rec(root,min,max):
    if root == None:
        return True
    if root.val<=min or root.val>=max:
        return False
    return rec(root.left,min,root.val) and rec(root.right,root.val,max)

tt = constructBST()
printTree(tt)
# global previous
previous = tt.val
print(isValidBST2(tt))
