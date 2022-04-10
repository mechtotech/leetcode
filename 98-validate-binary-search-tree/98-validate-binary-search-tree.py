# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        max of left subtree of node is less than node
        min of right subtree of node is greater than node
        
        
        # global problem is return if the tree is bst
        # local problem is 
        max of left subtree of node is less than node
        min of right subtree of node is greater than node
        
        return min & max of tree to its parent
        
        """
        if root is None:
            return None
        
        globalbst = [True]
        
            
        
        def dfs(node):
            amibst = True
            smallest = node.val
            largest=  node.val
            
            if node.left is None and node.right is None:
                pass
            
            
            if node.left:
                (s,l,b) = dfs(node.left)
                smallest = min(smallest,s)
                largest= max(largest,l)
                if b is False or l >= node.val :
                    amibst= False
                    
            if node.right:
                (s,l,b) = dfs(node.right)
                smallest = min(smallest,s)
                largest = max(largest,l)
                if b is False or s<= node.val:
                    amibst= False
            if amibst is False:
                globalbst[0] = False
            return (smallest,largest,amibst)
        dfs(root)
        return globalbst[0]
        
                
                
                
            
            
            
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        