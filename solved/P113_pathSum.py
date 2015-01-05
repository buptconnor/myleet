__author__ = 'Connor'
from TreeNode import constructdefault1
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root == None:
            return []
        ans = []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        else:
            if root.left != None:
                tmp = self.pathSum(root.left,sum-root.val)
                if tmp != []:
                   for item in tmp:
                       tt = [root.val]
                       tt.extend(item)
                       ans.append(tt)
            if root.right != None:
                tmp = self.pathSum(root.right,sum-root.val)
                if tmp != []:
                   for item in tmp:
                       tt =[root.val]
                       tt.extend(item)
                       ans.append(tt)
            return ans

def sumup(list):
    total = 0
    for i in list:
        total += i
    return total

if __name__ == '__main__':
    tt = constructdefault1()
    so = Solution()
    ans = (so.pathSum(tt,22))
    print(ans)
