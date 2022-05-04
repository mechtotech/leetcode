class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        
        def helper(s,i,slate):
            
            if i == len(s):
                result.append(slate[:])
                return
            hashmap = {}
            for pick in range(i,len(s)):
                if s[pick] not in hashmap:
                    hashmap[s[pick]] = 1
                    s[i],s[pick] = s[pick],s[i]
                    slate.append(s[i])
                    helper(s,i+1,slate)
                    slate.pop()
                    s[i],s[pick] = s[pick],s[i]
        helper(nums,0,[])
        return result
        
                
                
            
            
                
        
        
        
        