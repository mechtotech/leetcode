class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """
        15 - 12 =3
        15-12=3
        
        """
        
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1
            else:
                return nums[i]
            
        