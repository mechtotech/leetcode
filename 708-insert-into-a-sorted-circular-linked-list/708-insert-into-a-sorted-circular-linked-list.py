"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal,None)
        if head is None:
            head = node
            node.next = head
            return head
        elif head.next is None:
            node.next = head
            head.next = node
            return head
        
        
        
        prev= head
        curr= head.next
        
        while prev.val <= curr.val and curr != head:
            prev= curr
            curr=curr.next
        
        if curr.val >= node.val or prev.val < node.val:
            prev.next = node
            node.next = curr
            return head
        
        while node.val > curr.val:
            prev = curr
            curr = curr.next
           
        
        prev.next = node
        node.next = curr
        
        return head
        
        
        
        
        