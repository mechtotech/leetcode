class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}
        
        
        
        for i in range(len(nums)):
            if nums[i] not in count:
                left[nums[i]] = i
                count[nums[i]] = 1
                right[nums[i]] = i
            else:
                right[nums[i]] = i
                count[nums[i]] +=1
        
        length = len(nums)
      
        #currentlength = 0
        degree = max(count.values())
        for i in range(len(nums)):
            if  count[nums[i]] == degree:
                length = min(length,right[nums[i]]-left[nums[i]]+1)
        
        return length
                
                
                
            
            
        