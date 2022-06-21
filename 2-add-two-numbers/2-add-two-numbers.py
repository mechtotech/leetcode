# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        sentinel = ListNode("dummy")
        tail = sentinel
        
        curr1 = l1
        curr2 = l2
        
        carry = 0
        while curr1 and curr2:
            
            sum = curr1.val+ curr2.val +carry
            newnode = ListNode(sum%10)
            
            if sum > 9:
                carry = 1
            else:
                carry =0
            tail.next = newnode
            tail = tail.next
            
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            
            sum = curr1.val+carry
            newnode = ListNode(sum%10)
            if sum > 9:
                carry = 1
            else:
                carry =0
            tail.next = newnode
            tail = tail.next
            
            curr1 = curr1.next
        while curr2:
            
            sum = curr2.val+carry
            newnode = ListNode(sum%10)
            if sum > 9:
                carry = 1
            else:
                carry =0
            tail.next = newnode
            tail = tail.next
            
            curr2 = curr2.next
        
        if carry == 1:
            newnode = ListNode(carry)
            tail.next = newnode
            tail = tail.next
        
        
        return sentinel.next
            
            
            
            
            

            