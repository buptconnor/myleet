__author__ = 'Connor'
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def consturct(arr):
    if arr ==[]:
        return None
    head= ListNode(arr[0])
    p=head
    i=1
    while i<len(arr):
        p.next= ListNode(arr[i])
        p= p.next
        i+=1
    return head


def printll(head):
    p=head
    while p!=None:
        print(p.val)
        p=p.next
    return

# @param head, a ListNode
# @param k, an integer
# @return a ListNode
def rotateRight(head, k):
    if k == 0 or head == None:
        return head
    p = head
    length = 1
    while p.next != None:
        length += 1
        p = p.next
    k1 = k
    while k1 >=length:
        k1 -= length
    if k1 == 0:
        return head
    cnt = 0
    q = head
    while cnt< length-k1-1:
        q = q.next
        cnt += 1
    newhead = q.next
    q.next = None
    p.next = head
    return newhead

aa = [i+1 for i in range(5)]
ll = consturct(aa)
# printll(ll)
l2 = rotateRight(ll,5)
printll(l2)