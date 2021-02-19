# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def isListPalindrome(l):
    node = l
    # Append all nodes to form a string  
    temp = [] 
    while node : 
        temp.append(node.value) 
        node = node.next
    for i in range(len(temp) // 2):
        if temp[i] != temp[len(temp) - i - 1]:
            return False
    return True
  
