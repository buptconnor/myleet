__author__ = 'Connor'
from TreeNode import TreeNode
from TreeNode import consturctdefault

def hasPathSum( root, sum):
    if root ==None:
        return False
    ans = True
    if root.left == None and root.right == None:
        return root.val == sum
    else:
        if root.left != None:
            ans = hasPathSum(root.left,sum-root.val)
            if ans:
                return True
        if root.right != None:
            ans = hasPathSum(root.right,sum-root.val)
        return ans

tt = consturctdefault()
print(hasPathSum(tt,23))




