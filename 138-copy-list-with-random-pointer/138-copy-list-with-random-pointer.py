"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        
        curr = head
        while curr:
            node = Node(curr.val)
            node.next = curr.next
            curr.next= node
            curr = node.next
        
        curr = head
        
        while curr:
            if curr.random is not None:
                curr.next.random = curr.random.next
                curr = curr.next.next
            else:
                curr.next.random = None
                curr = curr.next.next
        
        curr = head
        curr1 = head.next
        newhead = head.next
        
        while curr and curr1:
            curr.next = curr.next.next
            if curr.next is not None:
                
                curr1.next = curr1.next.next
            else:
                curr1.next = None
            curr1 = curr1.next
            curr = curr.next
        return newhead
            
            
        
        
        
            
            
            
            