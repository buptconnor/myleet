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