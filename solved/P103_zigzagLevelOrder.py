__author__ = 'Connor'
from TreeNode import consturctdefault
#     3
#    / \
#   9  20
#     /  \
#    15   7
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        ans =[]
        p = root
        level = 0
        nextlevel = []
        if p != None:
            nextlevel.append(p)
        while nextlevel != []:
            tmp = []
            ans.append([])
            for node in nextlevel:
                ans[level].append(node.val)
                if node.left != None:
                    tmp.append(node.left)
                if node.right != None:
                    tmp.append(node.right)
            nextlevel = tmp
            if level %2 ==1:
                ans[level].reverse()
            level += 1
        return ans

if __name__ == '__main__':
    tt = consturctdefault()
    so = Solution()
    print(so.zigzagLevelOrder(tt))