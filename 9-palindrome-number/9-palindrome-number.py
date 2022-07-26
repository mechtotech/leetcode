class Solution:
    
    
    
    
    def isPalindrome(self, x: int) -> bool:
        
        
        
        if abs(x) != x:
            return False
        
        def reverse(x):
            
            r = 0
            
            while x>0:
                
                r = r*10 + x%10
                x //=10
            
            return r
        
        return x == reverse(x)
        
        
        
     