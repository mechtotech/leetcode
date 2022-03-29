# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        diameter = [0]
        
        def dfs(node):
            height = 0
            mydia=0
            
            if node.left is None and node.right is None:
                return 0
            
            
            if node.left :
                lh = dfs(node.left)
                height = lh+1
                mydia = lh+1
            
            
            if node.right:
                rh = dfs(node.right)
                height = max(height,rh+1)
                mydia += rh+1
            
            
            diameter[0] = max(mydia,diameter[0])
            
            
            
            
            
            return height
        
        dfs(root)
        return diameter[0]
        
        