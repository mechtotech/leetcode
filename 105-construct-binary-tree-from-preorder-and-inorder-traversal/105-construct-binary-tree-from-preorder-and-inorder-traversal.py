# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        m={}
        for i in range(len(inorder)):
            m[inorder[i]] = i
       
        def helper(p,startp,endp,i,starti,endi):
            if startp > endp:
                return None
            elif startp == endp:
                return TreeNode(p[startp])
            else:
                root = TreeNode(p[startp])
                rootindex = m[root.val]
                numleft = rootindex - starti
                numright = endi-rootindex
                root.left = helper(p,startp+1,startp+numleft,i,starti,rootindex-1)
                root.right = helper(p,startp+numleft+1,endp,i,rootindex+1,endi)
                
            return root
        return helper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
            
            
        
       