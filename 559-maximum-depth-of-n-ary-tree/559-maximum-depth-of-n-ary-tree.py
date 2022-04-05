"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        q = deque()
        q.append(root)
        level = 0
        while len(q) >0 :
            level +=1
            for _ in range(len(q)):
                node = q.popleft()
                
                for child in node.children:
                    q.append(child)
        
        return level
                
                
        