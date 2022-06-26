# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        newroot = [None]
        def dfs(node,parent,rightsibling):
            
            
            
            
            
            if node.left is None and node.right is None:
                node.left = rightsibling
                node.right = parent
                newroot[0] = node
                return
            
            oldleft = node.left
            oldright = node.right
            node.left = rightsibling
            node.right = parent
            
            if oldleft:
                
                dfs(oldleft,node,oldright)
            
            if oldright:
                pass
        
        dfs(root,None,None)
        return newroot[0]
                
            
            
            
        
        
        
        