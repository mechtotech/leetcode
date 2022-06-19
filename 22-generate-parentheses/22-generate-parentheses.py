class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def helper(left,right,slate):
            
            
            if left > right or left < 0 or right < 0:
                return
            
            if left == right == 0:
                result.append("".join(slate))
                return
            
            slate.append('(')
            helper(left-1,right,slate)
            slate.pop()
            
            slate.append(')')
            helper(left,right-1,slate)
            slate.pop()
        
        helper(n,n,[])
        return result
        