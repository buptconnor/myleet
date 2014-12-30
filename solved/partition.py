__author__ = 'Connor'
from ListNode import ListNode as ListNode
from ListNode import consturct
from ListNode import printll


# @return a ListNode
def partition(head, x):
    if head == None:
        return head
    p = head
    smallfront = None
    smallend = None
    bigfront = None
    bigend = None

    while p!=None:
        if p.val < x:
            if smallfront == None:
                smallfront = ListNode(p.val)
                smallend = smallfront
            else:
                smallend.next = ListNode(p.val)
                smallend = smallend.next
        else:
            if bigfront == None:
                bigfront = ListNode(p.val)
                bigend = bigfront
            else:
                bigend.next = ListNode(p.val)
                bigend = bigend.next
        p = p.next
    if smallend !=None:
        smallend.next = bigfront
        return smallfront
    else:
        return bigfront

aa =[1]# [1,4,3,2,5,2]
ll = consturct(aa)
ans = partition(ll,3)
printll(ans)
