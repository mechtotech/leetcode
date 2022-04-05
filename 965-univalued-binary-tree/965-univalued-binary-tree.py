# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        result = []
        q= deque()
        q.append(root)
        unival = root.val
       
        while len(q) !=0:
            
            node =q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            if node.val != unival:
                return False
        return True
        
        