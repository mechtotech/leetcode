# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            left = None
            
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if left is None:
                    left = node.val
        
        return left
        