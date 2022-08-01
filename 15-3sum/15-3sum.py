class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output =[]
        
        
        def function(nums,k):
            
            
            i = k+1
            j = len(nums)-1
            
            while i < j:
                
                if nums[i]+nums[j]+nums[k] == 0:
                    output.append([nums[i],nums[j],nums[k]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i-1]:
                        i+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    j-=1
                else:
                    i+=1
        
        for k in range(len(nums)):
            
            if k == 0 or nums[k] != nums[k-1]:
                function(nums,k)
        return output
        
        
        
                    
                    
        