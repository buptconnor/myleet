__author__ = 'Connor'

from TreeNode import TreeNode
from TreeNode import printTree
import ListNode
from ListNode import consturct

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        size = 0
        p = head
        while p != None:
            size += 1
            p = p.next
        locate_root = int(size/2)
        cnt = 0
        p = head
        while cnt < locate_root-1:
            cnt += 1
            p = p.next
        if p.next != None:
            root = TreeNode(p.next.val)
            root.right = self.sortedListToBST(p.next.next)
            p.next = None
            root.left = self.sortedListToBST(head)
            return root
        else:
            return TreeNode(p.val)


if __name__ == '__main__':
    so = Solution()
    aa =[1,2,3,4,5]
    ll = consturct(aa)
    tt = so.sortedListToBST(ll)
    printTree(tt)