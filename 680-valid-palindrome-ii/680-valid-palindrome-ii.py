class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(i,j):
            return s[i:j+1]==s[i:j+1][::-1]
        
        i = 0
        j = len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                first = isPalindrome(i+1,j)
                if first is True:
                    return True
                second = isPalindrome(i,j-1)
                return second
            
            i+=1
            j-=1
            
            
        return True
                
                
            
            
            
            
           
        
        