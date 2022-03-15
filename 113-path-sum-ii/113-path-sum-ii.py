# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        if root is None:
            return []
        
        result =[]
        def dfs(node,target,slate):
            slate.append(node.val)
            if node.left is None and node.right is None:
                
                if node.val == target:
                    #slate.append(node.val)
                    result.append(slate[:])
                    #slate.pop()
            
            
            
            if node.left:
                #slate.append(node.val)
                dfs(node.left,target-node.val,slate)
                #slate.pop()
               
            if node.right:
                #slate.append(node.val)
                dfs(node.right,target-node.val,slate)
                #slate.pop()
            slate.pop()
        
        
        dfs(root,targetSum,[])
        return result
                    

        
        