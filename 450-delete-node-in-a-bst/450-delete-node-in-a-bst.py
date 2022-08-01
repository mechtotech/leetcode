# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def succ(self,root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    def pred(self,root):
        
        root = root.left
        while root.right:
            root = root.right
        return root.val
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.succ(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.pred(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
    
        
    
    
    
    
    
   
