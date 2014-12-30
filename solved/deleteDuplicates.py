__author__ = 'Connor'
import ListNode
from ListNode import consturct
from ListNode import printll

def deleteDuplicates(head):
    if head == None or head.next == None:
        return head
    p = head
    cur = p.val
    while p.next!=None:
        if p.next.val == cur:
            p.next=p.next.next
        else:
            p=p.next
            cur = p.val
    return head

# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
def deleteDuplicates2(head):
    if head == None or head.next == None:
        return head
    p = head
    cur = p.val
    dup = False
    lastHead = None
    lastDis = None
    while p.next != None:
        if p.next.val == cur:
            dup = True
            p=p.next
        elif not dup:
            if lastDis == None:
                lastHead = ListNode.ListNode(p.val)
                lastDis = lastHead
            else:
                lastDis.next = ListNode.ListNode(p.val)
                lastDis = lastDis.next
            p = p.next
            cur = p.val
            dup = False
        else:
            p = p.next
            cur = p.val
            dup = False

    if not dup:
        if lastDis == None:
                lastHead = ListNode.ListNode(p.val)
                lastDis = lastHead
        else:
            lastDis.next=ListNode.ListNode(p.val)
    return lastHead


aa = [1,8,8]
ll = consturct(aa)
# printll(ll)
bb = deleteDuplicates2(ll)
printll(bb)