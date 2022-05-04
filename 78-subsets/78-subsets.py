class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==0:
            return [[]]
        result = []
        
        def helper(s,i,slate):
            if i == len(s):
                result.append(slate[:])
                return
            
            helper(s,i+1,slate)
            slate.append(s[i])
            helper(s,i+1,slate)
            slate.pop()
        
        helper(nums,0,[])
        return result
            
            
        
        