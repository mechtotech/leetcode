# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        """
        
        local problem calculate if the node has bst node
        
        
        """
        if root is None:
            return 0
        
        
        largestbst = [0]
        def dfs(node):
            
            amibst = True
            smallest = node.val
            largest = node.val
            size = 1
            
            if node.left is None and node.right is None:
                pass
            
            if node.left:
                
                (s,l,b,sz) = dfs(node.left)
                size +=sz
                largest = max(largest,l)
                smallest = min(smallest,s)
                if not b or l >=node.val:
                    amibst = False
            if node.right:
                (s,l,b,sz) = dfs(node.right)
                size +=sz
                largest = max(largest,l)
                smallest = min(smallest,s)
                if not b or s <=node.val:
                    amibst = False
            if amibst :
                largestbst[0] = max(largestbst[0],size)
                
            return (smallest,largest,amibst,size)
        dfs(root)
        return largestbst[0]
                
                    
                
                
                
            
            
            
            
            
            
            
        
        