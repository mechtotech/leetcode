# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        
        result = []
        q = deque()
        q.append(root)
        
        while len(q) >0 :
            numnodes = len(q)
            temp = 0
            for _ in range(numnodes):
                node = q.popleft()
                temp+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(temp/numnodes)
        return result
            
                
        