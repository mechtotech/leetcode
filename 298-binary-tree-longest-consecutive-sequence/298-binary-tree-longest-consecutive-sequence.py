# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        
        
        globalcount = [0]
        def dfs(node,p,count):
            
            
            if node.val == p+1:
                count+=1
            else:
                count=1
            
            globalcount[0] = max(globalcount[0],count)
                
            
            
            if node.left is None and node.right is None:
                pass
                
            
            
    
            if node.left:
                dfs(node.left,node.val,count)
                
            if node.right:
                dfs(node.right,node.val,count)
        
        dfs(root,-float('inf'),1)
        return globalcount[0]
        
        