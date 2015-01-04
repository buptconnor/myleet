__author__ = 'Connor'
from TreeNode import consturctdefault

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        stack = [[root]]
        while stack[len(stack)-1]  != []:
            tmp =[]
            for i in stack[len(stack)-1]:
                if i.left != None:
                    tmp.append(i.left)
                if i.right != None:
                    tmp.append(i.right)
            stack.append(tmp)
        ans =[]
        stack.pop()
        while stack != []:
            level = stack.pop()
            tmp = []
            for i in level:
                tmp.append(i.val)
            ans.append(tmp)
        return ans




if __name__ == '__main__':
    tt = consturctdefault()
    so = Solution()
    print(so.levelOrderBottom(tt))