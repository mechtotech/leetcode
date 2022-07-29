class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.big = nums[:k] if k < len(nums) else nums
        heapq.heapify(self.big)
        self.k = k
    def add(self, val):
        heapq.heappush(self.big, val)
        if len(self.big) > self.k: #keep k largest elements in the heap
            heapq.heappop(self.big)
        return self.big[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)