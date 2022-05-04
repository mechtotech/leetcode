class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return None
        nums.sort()
        result = []
        def helper(s,i,slate):
            if i == len(s):
                result.append(slate[:])
                return
            
            count = 0
            for pick in range(i,len(s)):
                if s[pick]==s[i]:
                    count +=1
            helper(s,i+count,slate)
            for c in range(count):
                slate.append(s[i])
                helper(s,i+count,slate)
            for c in range(count):
                slate.pop()
            
        helper(nums,0,[])
        return result
                    
            
            
            
        
        
        
        