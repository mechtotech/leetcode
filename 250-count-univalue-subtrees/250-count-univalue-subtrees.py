# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        unival = [0]
        def dfs(node):
            amiunival = True
            
            
            
            if node.left is None and node.right is None:
                unival[0]+=1
                return True
                
            
            if node.left:
                L = dfs(node.left)
                if L is False or node.val != node.left.val:
                    amiunival = False
            
            if node.right:
                R= dfs(node.right)
                if R is False or node.val != node.right.val:
                    amiunival = False
            
            if amiunival:
                unival[0]+=1
            
            return amiunival
        
        dfs(root)
        return unival[0]
                
        
        