__author__ = 'Connor'
from TreeNode import TreeNode
from TreeNode import printTree

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if inorder == []:
            return None
        root = TreeNode(postorder[len(postorder)-1])
        length = inorder.index(postorder[len(postorder)-1])
        if length != len(postorder)-1:
            root.right = self.buildTree(inorder[length+1:],postorder[length: len(postorder)-1])
        if length > 0:
            root.left = self.buildTree(inorder[:length],postorder[:length])
        return root


if __name__ == '__main__':
    postOrder = [7,4,2,5,8,6,3,1]
    inOrder = [4,7,2,1,5,3,8,6]
    so = Solution()
    ans = so.buildTree(inOrder,postOrder)
    printTree(ans)