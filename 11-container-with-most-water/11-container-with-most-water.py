class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 1:
            return 0
        
        maxarea = -float('inf')
        
        i = 0
        j = len(height)-1
        
        while i < j:
            
            width = j-i
            maxarea= max(maxarea,min(height[i],height[j])*width)
            
            if height[i] <=height[j]:
                i+=1
            else:
                j-=1
        return maxarea
            
            
            
            
                
            
        
        
        
        
            
        
    
                
                
                
                
                
            
        