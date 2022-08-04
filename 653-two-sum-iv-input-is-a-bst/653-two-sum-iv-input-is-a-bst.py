# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        """
        m = {target-node.val }
        
        
        
        
        """
        
        
        m={}
        flag = [False]
        
        def dfs(node):
            
            difference = k - node.val
            if difference in m:
                flag[0] = [True]
            else:
                m[node.val] = 1
                
            
                
            
            
            if node.left is None and node.right is None:
                pass
                
            
            
            if node.left:
                dfs(node.left)

                
                
            if node.right:
                dfs(node.right)
        dfs(root)
        return flag[0]
                
                
                
                
                
        