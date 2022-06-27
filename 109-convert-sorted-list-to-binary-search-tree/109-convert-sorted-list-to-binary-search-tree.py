# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head is None:
            return None
        
        curr = head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr = curr.next
        #print(arr)
        def helper(a,start,end):
            
            if start > end:
                return None
            
            elif start == end:
                return TreeNode(a[start])
            
            else:
                mid= (start+end) //2
                root = TreeNode(a[mid])
            
                root.left = helper(a,start,mid-1)
                root.right = helper(a,mid+1,end)
                
            
            return root
        return helper(arr,0,len(arr)-1)
        
        
        
            

            
            
        
        
        