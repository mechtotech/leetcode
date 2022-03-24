# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result =deque()
        q = deque()
        q.append(root)
        while len(q) >0:
            temp =[]
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.appendleft(temp)
        
        return result
            
            
                    
        
        
        
        
        
        
        
        
        
        