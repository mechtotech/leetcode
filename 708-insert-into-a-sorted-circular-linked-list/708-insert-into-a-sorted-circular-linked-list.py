"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = ListNode(insertVal,None)
        
        if head is None:
            node.next = node
            return node
        elif head.next is None:
            node.next = head
            head.next = node
            
            return head
        
        # find the first element -smallest and last element - largest value node
        # insert the node - ascending order - node.val= insertVal > curr.val head -prev.next = node
        #node = curr.next
        # insertval is actaully largest prev.next = node & node.mext = 
        
        prev = head
        curr = head.next
        
        while prev.val <= curr.val and curr!= head:
            prev = prev.next
            curr = curr.next
        #prev is last node and curr is smallest node
            
        if insertVal > prev.val :
            prev.next = node
            node.next = curr
            return head
      
        while insertVal > curr.val:
            prev = curr
            curr = curr.next
            
            
        prev.next = node
        node.next = curr
        
        
        return head
            
            
            
            