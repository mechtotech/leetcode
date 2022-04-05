# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        
        q = deque()
        result = []
        q.append(root)
        level = 0 
        while len(q) > 0:
            temp = []
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    if node.left:
                        q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level%2 != 0:
                result.append(temp)
            else:
                result.append(temp[::-1])
        
        return result
        
            
                
                
        
        
        
        