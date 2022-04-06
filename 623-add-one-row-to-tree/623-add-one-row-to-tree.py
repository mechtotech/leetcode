# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newroot = TreeNode(val)
            newroot.left = root
            #root = newroot
            return newroot
        
        
        q = deque()
        q.append(root)
        level = 0
        
        while len(q) >0:
            
            level +=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if level == depth-1:
                    oldleft = node.left
                    oldright = node.right
                    newleft = TreeNode(val)
                    newright = TreeNode(val)
                    newleft.left = oldleft
                    newright.right = oldright
                    node.left = newleft
                    node.right = newright
                    
        
        return root
                    
                    
                
        
        