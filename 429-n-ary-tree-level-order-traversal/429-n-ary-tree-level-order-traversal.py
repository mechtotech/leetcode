"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None:
            return []
        
        result = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            numnodes= len(q)
            temp = []
            for i in range(numnodes):
                
                node = q.popleft()
                temp.append(node.val)
                for child in node.children:
                    q.append(child)
            result.append(temp)
        return result
    
        
        
        
        