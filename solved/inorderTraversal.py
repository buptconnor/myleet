__author__ = 'Connor'
from TreeNode import consturctdefault
from TreeNode import printTree

# @param root, a tree node
# @return a list of integers
def inorderTraversal(root):
    p = root
    ans = []
    stack = []
    while p !=None or stack != []:
        while p!=None:
            stack.append(p)
            p = p.left
        if stack != []:
            p = stack.pop()
            ans.append(p.val)
            p = p.right
    return  ans
tt = consturctdefault()
printTree(tt)
ans = inorderTraversal(tt)
print(ans)