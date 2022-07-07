class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.maxsize = size
        self.sum = 0

    def next(self, val: int) -> float:
        
        if self.maxsize > len(self.q):
            self.q.append(val)
            self.sum += val
            
        else:
            popped=self.q.popleft()
            self.q.append(val)
            self.sum += val
            self.sum -=popped
        
        return self.sum/len(self.q)
        
            
    
        
        
        
        
            
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)