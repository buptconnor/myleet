__author__ = 'Connor'

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
def construct(A):
    beforehead = RandomListNode(-1)
    p = beforehead
    for a in A:
        p.next = RandomListNode(a)
        p = p.next
    p = beforehead.next
    return beforehead.next

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        p = head
        while p != None:
            tmp = p.next
            pcopy = RandomListNode(p.label)
            pcopy.next = tmp
            p.next = pcopy
            p = p.next.next
        q = head
        while q != None:
            if q.random != None:
                q.next.random = q.random.next
            q = q.next
        nhead = head.next
        pn = nhead
        po = head
        while po != None:
            po.next = pn.next
            po = po.next
            pn.next = po.next
            pn = pn.next
        po .next = None
        pn.next = None
        return nhead

if __name__ == '__main__':
    so =Solution()
