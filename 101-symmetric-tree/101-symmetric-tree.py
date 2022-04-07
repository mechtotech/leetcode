# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        q = deque()
        q.append((root,root))
        while len(q) > 0:
            for _ in range(len(q)):
                (nl,nr) = q.popleft()
                if nl.left and nr.right:
                    q.append((nl.left,nr.right))
                elif (nl.left is None and nr.right)  or (nl.left and nr.right is None):
                    return False
                if nl.right and nr.left:
                    q.append((nl.right,nr.left))
                elif  nr.left or nl.right :
                    return False
                
                
                
                if nl.val != nr.val:
                    return False
        return True
                    
                
                    