import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def helper(nums,start,end,k):
            if start > end:
                return
            pivot = random.randint(start,end)
            nums[pivot],nums[start] = nums[start],nums[pivot]
            orange = start
            for green in range(start+1,end+1):
                if nums[green] < nums[start]:
                    orange +=1
                    nums[green],nums[orange] = nums[orange],nums[green]
            nums[orange],nums[start] = nums[start],nums[orange]
            if len(nums)-k == orange:
                return nums[len(nums)-k]
            elif len(nums)-k  < orange:
                return helper(nums,start,orange-1,k)
            else:
                return helper(nums,orange+1,end,k)
 
        return helper(nums,0,len(nums)-1,k)
    