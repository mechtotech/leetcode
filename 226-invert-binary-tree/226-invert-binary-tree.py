# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        
        def dfs(node):
            
            
            oldleft = node.left
            oldright = node.right
            node.left = oldright
            node.right = oldleft
            
            if node.left is None and node.right is None:
                pass
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
        
        dfs(root)
        return root
            
            
        