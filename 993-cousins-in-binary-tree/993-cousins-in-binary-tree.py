# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        q =deque()
        q.append(root)
        
        px = None
        py = None
        while len(q) !=0:
            numnodes = len(q)
            #temp = []
            for i in range(numnodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if node.left.val == x:
                        px = node.val
                    if node.left.val == y:
                        py = node.val
                if node.right:
                    q.append(node.right)
                    if node.right.val == x:
                        px = node.val
                    if node.right.val == y:
                        py = node.val
            if px is not None or py is not None:
                return px !=py and py is not None and px is not None
            
        
        
        