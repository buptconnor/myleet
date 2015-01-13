__author__ = 'Connor'

from ListNode import ListNode
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        lenA = 1
        lenB = 1
        p = headA
        while p.next != None:
            p = p.next
            lenA += 1
        q = headB
        while q.next != None:
            q = q.next
            lenB += 1
        if q != p:
            return None
        dif = abs(lenA - lenB)
        p = (headA if lenA >= lenB else headB)
        q = (headB if lenA >= lenB else headA)
        cnt = 0
        while cnt < dif :
            p = p.next
            cnt += 1
        while p != q:
            p = p.next
            q = q.next
        return p
def constructIntersection():
    p2 = ListNode(2)
    p3 = ListNode(3)
    p2.next = p3
    return p2,p3
if __name__ == '__main__':
    l1,l2 = constructIntersection()
    so = Solution()
    ll = so.getIntersectionNode(l1,l2)
    print(ll.val)