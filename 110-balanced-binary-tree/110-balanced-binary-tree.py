# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        globalbbt = [True]
        def dfs(node):
            amibbt = True
            myheight = 0
            if node.left is None and node.right is None:
                return 0
            LH = 0
            RH =0
            if node.left:
                LH = dfs(node.left)+1
                
                 
            if node.right:
                RH=  dfs(node.right)+1
            myheight = max(LH,RH)
            if abs(LH-RH) > 1:
                amibbt = False
                globalbbt[0] = False
            
                
            return myheight
        dfs(root)
        return globalbbt[0]
    
    

                
                
                
                
            
            
        
        