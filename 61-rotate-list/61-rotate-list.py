# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        """
        find length of the list
        find green = l-k%length
        while loop till curr - green+1 followed by prev = green
        prev.next = None
        curr is new head
        
        
        
        
        """
        if head is None or head.next is None:
            return head
        
        sentinel = ListNode("dummy",head)
        #tail =sentinel
        curr = head
        length = 0
        while curr:
            length+=1
            prev = curr
            curr = curr.next
        
        green = length -(k%length)
        if length == green:
            return head
        
        i=0
        curr2 = head
        prev2= sentinel
        while curr2 and i < green:
            i+=1
            prev2= curr2
            curr2 = curr2.next
        
        prev2.next = None
        prev.next = sentinel.next
        sentinel.next = curr2
        
        
        return sentinel.next
        
        
        
        
        