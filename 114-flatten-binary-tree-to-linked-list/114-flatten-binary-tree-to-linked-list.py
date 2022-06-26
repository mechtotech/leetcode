# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        
        local problem connect preorder traversal to sentinel
        """
        if root is None:
            return None
       
        sentinel = TreeNode("dummy")
        
        def dfs(node,pred):
            
            if node.left is None and node.right is None:
                pred.left = node
                pred = node
                return pred
            
        
            pred.left= node
            pred = node
            
            
            if node.left:
                pred = dfs(node.left,pred)
            if node.right:
                pred= dfs(node.right,pred)
                
            return pred
        
        dfs(root,sentinel)
        
        curr = sentinel.left
        while curr:
            curr.right = curr.left
            curr.left = None
            curr = curr.right
        
        return sentinel.left
            
        
            
                
        
        
            
        
        