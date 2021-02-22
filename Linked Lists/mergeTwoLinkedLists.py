# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    p = l1
    q = l2
    new_head   = ListNode(0)
    soting = None
    
    if q == None:
        return p
    if p == None:
        return q
    if (p and q):
        if p.value <= q.value:
            sorting = p
            p = sorting.next
        else:
            sorting = q
            q = sorting.next
            
    new_head = sorting
    
    while(p and q):
        if p.value <= q.value:
            sorting.next = p
            sorting = p
            p = sorting.next
        else:
            sorting.next = q
            sorting = q
            q = sorting.next
    if p == None:
        sorting.next = q
    if q == None:
        sorting.next = p
            
    return new_head
