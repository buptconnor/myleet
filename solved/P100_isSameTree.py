__author__ = 'Connor'
from TreeNode import consturctdefault
from TreeNode import constructBST

class Solution:
    def isSameTree(self,p,q):
        sp = NodeStructure(p)
        sq = NodeStructure(q)
        if sp != sq:
            return False
        elif sp == -1:
            return True
        else:
            if sp == 1:
                return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            elif sp == 2:
                return p.val == q.val and self.isSameTree(p.right,q.right)
            elif sp == 3:
                return p.val == q.val and self.isSameTree(p.left,q.left)
            elif sp == 0:
                return p.val == q.val

def NodeStructure(p):
    if p == None:
        return -1
    if p.left != None and p.right != None:
        return 1
    elif p.left == None and p.right != None:
        return 2
    elif p.left!= None and p.right == None:
        return 3
    elif p.left == None and p.right == None:
        return 0

if __name__ == '__main__':
    t1 = consturctdefault()
    t2 = consturctdefault()
    t3 = constructBST()
    so = Solution()
    ans = so.isSameTree(t1,t3)
    print(ans)