class NumArray:

    def __init__(self, nums: List[int]):

        self.prefix = []
        self.m = {}
        self.prefixsum = 0
        for i in range(len(nums)):
            self.prefixsum += nums[i]
            self.prefix.append(self.prefixsum)
            

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left-1]
        
        
        
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)