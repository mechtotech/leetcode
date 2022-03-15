# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None:
            return 0
        
        
        path =[0]  # global problem
        
        def dfs(node):
            
            longestpath = 0
            longestvpath = 0
            
            if node.left is None and node.right is None:
                pass
            
            if node.left:
                LL=dfs(node.left)
                if node.val == node.left.val:
                    longestpath = LL+1
                    longestvpath = LL+1
            
            if node.right:
                LR = dfs(node.right)
                if node.val == node.right.val:
                    longestpath = max(longestpath,1+LR)
                    longestvpath+= 1+LR
            
            
            path[0] = max(longestvpath,path[0])
            return longestpath
            
        
        dfs(root)
        return path[0]
                
            
            
        