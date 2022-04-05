# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        
        result = []
        q = deque()
        q.append(root)
        
        while len(q) >0 :
            numnodes = len(q)
            temp = None
            for _ in range(numnodes):
                node = q.popleft()
                temp=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(temp)
        return result
        