class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []
        
        
        
        def function(nums,x):
            
            i = x+1
            j = len(nums)-1
            
            while i < j:
                
                if nums[x]+nums[i]+nums[j] == 0:
                    
                    output.append([nums[x],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    
                elif nums[x]+nums[i]+nums[j] > 0:
                    j-=1
                else:
                    i+=1
        for x in range(len(nums)):
            
            if x == 0 or nums[x-1] != nums[x]:
                function(nums,x)
        
        return output
                    
                    
        