# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        zero = []
        pos= []
        neg = []
        
        q = deque()
        q.append((root,0))
        while len(q) > 0:
            node,x = q.popleft()
            if x == 0:
                zero.append(node.val)
            elif x > 0 :
                if x > len(pos):
                    pos.append([])
                pos[x-1].append(node.val)
            else:
                if abs(x) > len(neg):
                    neg.append([])
                neg[abs(x)-1].append(node.val)
            if node.left:
                q.append((node.left,x-1))
            if node.right:
                q.append((node.right,x+1))
                
        
        neg.reverse()
        neg.append(zero)
        return neg + pos
                
        
        