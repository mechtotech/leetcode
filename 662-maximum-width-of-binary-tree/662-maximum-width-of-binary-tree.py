# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 1
        
        q = deque()
        q.append((root,1))
        result =[]
        

        while len(q) > 0:
            first  = None
            last= None
            
        
            for _ in range(len(q)):
                (node,id) = q.popleft()
                
                if node.left:
                    q.append((node.left,2*id))
                if node.right:
                    q.append((node.right,2*id+1))
                    
                if first is None:
                    first = id
                last = id
            result.append(last-first+1)
        return max(result)
                
                
        
        