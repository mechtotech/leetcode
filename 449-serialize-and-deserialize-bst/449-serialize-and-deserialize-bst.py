# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Enc
        odes a tree to a single string.
        
        """
        if root is None:
            return ""
        result = []
        def helper(node):
            
            result.append(str(node.val))
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            
        helper(root)
        return ",".join(result)
                
        
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        
        splitdata = data.split(",")
        preorder = [int(i) for i in splitdata]
        inorder = sorted(preorder)
        m = {}
        for i in range(len(inorder)):
            m[inorder[i]] = i
        
        def helper(i,starti,endi,p,startp,endp):
            
            if startp > endp:
                return
            
            elif startp == endp:
                return TreeNode(p[startp])
            
            
            else:
                root  = TreeNode(p[startp])
                rootindex = m[root.val]
                numleft = rootindex-starti
                numright = endi - rootindex
                
                root.left = helper(i,starti,rootindex-1, p,startp+1,startp+numleft)
                root.right = helper(i,rootindex+1,endi,p,startp+numleft+1,endp)
            return root
        return helper(inorder,0,len(inorder)-1,preorder,0,len(preorder)-1)
        
    
                
                
                
                
                
                
            
            
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans