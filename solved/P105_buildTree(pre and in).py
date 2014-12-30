__author__ = 'Connor'
from TreeNode import TreeNode
from TreeNode import printTree
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        length = inorder.index(preorder[0])
        if length != 0:
            root.left = self.buildTree(preorder[1:length+1],inorder[:length])
        if len(preorder) > length:
            root.right = self.buildTree(preorder[length+1:],inorder[length+1:])
        return root

if __name__ == '__main__':
    preOrder = [1,2,4,7,3,5,6,8]
    inOrder = [4,7,2,1,5,3,8,6]
    so = Solution()
    ans = so.buildTree(preOrder,inOrder)
    print(ans)
    printTree(ans)