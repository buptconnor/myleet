__author__ = 'Connor'
from ListNode import ListNode
from ListNode import consturct
from ListNode import printll

def reverseBetween(head,m,n):
    if m == n:
        return head
    p = head
    index = 1
    rehead = None
    reend = None
    if m == 1:
        return reversek(head,n-m)
    while p!=None and index<n:
        if index == m-1:
            rehead = p
            rehead.next = reversek(p.next,n-m)
            return head
        index += 1
        p = p.next

def reversek(head,k):
    p = head
    q = p.next
    i = 0
    tmp = None
    while i < k :
        tmp = q.next
        q.next = p
        p = q
        q = tmp
        i += 1
    head.next = tmp
    return p


aa = [1,2,3,4,5]
aa =[3,5,7]
ll = consturct(aa)
ans = reverseBetween(ll,1,2)
# ans = reversek(ll,3)
printll(ans)