__author__ = 'Connor'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def consturctdefault():
    root = TreeNode(5)
    lc = TreeNode(4)
    rc = TreeNode(8)
    root.left = lc
    root.right = rc
    lc.left = TreeNode(11)
    lc = lc.left
    lc.left = TreeNode(7)
    lc.right = TreeNode(2)
    rc.left = TreeNode(13)
    rc.right = TreeNode(4)
    rc = rc.right
    rc.right = TreeNode(1)
    return root

def constructdefault1():
    root = TreeNode(5)
    lc = TreeNode(4)
    rc = TreeNode(8)
    root.left = lc
    root.right = rc
    lc.left = TreeNode(11)
    lc = lc.left
    lc.left = TreeNode(7)
    lc.right = TreeNode(2)
    rc.left = TreeNode(13)
    rc.right = TreeNode(4)
    rc = rc.right
    rc.left = TreeNode(5)
    rc.right = TreeNode(1)
    return root

def constructBST():
    root =TreeNode(3)
    p1 =  TreeNode(1)
    p2 = TreeNode(5)
    p3 = TreeNode(0)
    p4 = TreeNode(2)
    p5 = TreeNode(4)
    p6 = TreeNode(6)

    root.left = p1
    root.right = p2
    p1.left = p3
    p1.right = p4
    p2.left = p5
    p2.right = p6
    return root

def constructSymmeric():
    root = TreeNode(1)
    p1 = TreeNode(2)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(4)
    p6 = TreeNode(3)

    root.left = p1
    root.right = p2
    p1.left = p3
    p1.right = p4
    p2.left = p5
    p2.right = p6
    return root

def printTree(root):
    p = root
    print(p.val)
    if p.left!=None:
        printTree(p.left)
    if p.right != None:
        printTree(p.right)


def preOrder(root):
    ans = []
    p = root
    stack = []
    while p != None or stack != []:
        while p != None:
            stack.append(p)
            ans.append(p.val)
            p=p.left
        if stack != []:
            p = stack.pop()
            p = p.right
    return ans


if __name__ == '__main__':
    tt = consturctdefault()
    printTree(tt)
