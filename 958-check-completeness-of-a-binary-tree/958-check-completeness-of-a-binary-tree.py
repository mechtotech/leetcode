# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        
        q = deque()
        q.append((root,1))
        expectedid = 1
        while len(q) > 0:
            
            for _ in range(len(q)):
                node,id = q.popleft()
                if id == expectedid:
                    expectedid +=1
                else:
                    return False
                if node.left:
                    q.append((node.left,2*id))
                if node.right:
                    q.append((node.right,2*id+1))
            
        return True
        
        
        
        