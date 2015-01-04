__author__ = 'Connor'
from TreeNode import TreeNode
from TreeNode import printTree
class Solution:
    # @return a list of tree node
    def generateTrees(self, n):

        return  gen(1,n)
def gen(l,r):
    if l> r:
        return [None]
    ans =[]
    for i in range(l,r+1):

        ltrees = gen(l,i-1)
        rtrees = gen(i+1,r)
        for j in range(len(ltrees)):
            for k in range(len(rtrees)):
                 root = TreeNode(i)
                 root.left = ltrees [j]
                 root.right = rtrees [k]
                 ans.append(root)

        # if ltrees != [None]:
        #     for lt in ltrees:
        #         root.left = lt
        #         if rtrees != [None]:
        #             for rt in rtrees:
        #                 root.right = rt
        #                 ans.append(root)
        #         else:
        #             root.right = None
        #             ans.append(root)
        # else:
        #     root.left = None
        #     if rtrees != [None]:
        #         for rt in rtrees:
        #             root.right = rt
        #             ans.append(root)
        #     else:
        #         root.right = None
        #         ans.append(root)
    return ans

if __name__ == '__main__':
    so = Solution()
    ans = so.generateTrees(3)
    cnt = 0
    print(ans)
    for i in ans:
        cnt += 1
        print('Num'+str(cnt))
        printTree(i)