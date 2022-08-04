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
       
        
        sentinelo = Node(-1000)
        tailo = sentinelo
        sentineln = Node(-1000)
        tailn = sentineln
        
        index = 0
        while curr:
            
            if index%2 == 0:
                tailo.next = curr
                tailo = curr
                
                curr = curr.next
                tailo.next = None
                index+=1
                
            else:
                tailn.next = curr
                tailn = curr
                #tailn.next = None
                curr = curr.next
                tailn.next = None
                index+=1
        return sentineln.next
        
                
            
            
        
        
        
        
            
            
        
        
        
            
            
            
            