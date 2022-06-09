# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        curr1 = l1
        curr2 = l2
        
        sentinel = ListNode("dummy")
        tail = sentinel
        carry = 0
        while curr1 and curr2:
            value = curr1.val + curr2.val + carry
            if value > 9:
                carry = 1
            else:
                carry = 0
            node = ListNode(value%10,None)
            tail.next = node
            tail = tail.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            value = curr1.val + carry
            if value > 9:
                carry = 1
            else:
                carry = 0
            
            node = ListNode(value%10,None)
            tail.next = node
            tail = tail.next
            curr1 = curr1.next
            
        while curr2:
            value = curr2.val + carry
            if value > 9:
                carry = 1
            else:
                carry = 0
            node = ListNode(value%10,None)
            tail.next = node
            tail = tail.next
            curr2 = curr2.next
        
        if carry != 0:
            node = ListNode(carry,None)
            tail.next = node
            tail = tail.next
        
        return sentinel.next
            
            
            
            
            
        
        
        
        
        