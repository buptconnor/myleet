__author__ = 'Connor'
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

def swapPairs(head):
    if head == None:
        return head
    pre=head
    p=head.next
    if p==None:
        return head
    q=p.next
    head=p
    pre.next=q
    head.next=pre

    while q!=None:
        p=q.next
        if p==None:
            return head
        pre.next=p
        q.next=p.next
        p.next=q
        pre=q
        q=q.next
    return head
# arr=[1,2]
# head= consturct(arr)
# printll(head)
# h=swapPairs(head)
# printll(h)

