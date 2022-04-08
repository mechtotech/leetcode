# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        """
        left + leaves + right
        
        left:
        1) root node
        2) root.left is not None add to left array 
        if no noder.left but node.right until it becomes a leaf node
        pop the last element
        
        right:
        
        add root.right is not none  to right array
        if no node.right but node.lleft until it becomes leaf
        pop the last element
        
        leaves
        use dfs
        anytime its leaf node campture it in array leaves
        
        
        return left + leaves + right.reverese()
        
        """
        
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        
        left =[root.val]
        
        if root.left:
            curr = root.left
            while curr:
                left.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr=curr.right
            left.pop()
        right =[]
        if root.right:
            curr= root.right
            while curr:
                right.append(curr.val)
                if curr.right:
                    curr=curr.right
                else:
                    curr=curr.left
            right.pop()
        right.reverse()
        leaves=[]
        
        def dfs(node):
            if node.left is None and node.right is None:
                leaves.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        
        return left +leaves + right