# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        
        result =[False]
        def dfs(node,target):
            
            if node.left is None and node.right is None:
                if node.val == target:
                    result[0] =True
            
            
            
            if node.left:
                dfs(node.left,target-node.val)
            if node.right:
                dfs(node.right,target-node.val)
        
        
        
        dfs(root,targetSum)
        return result[0]
