class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
        x = abs(x)
        nums = 0
        while x > 0:
            
            nums = nums*10 + x%10
            x = x//10
        
        if (-2**31 <= nums < 2**31) == False:
            return 0
        
        return nums*sign
            
            
        
            