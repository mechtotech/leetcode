class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.maxsize = size
        self.total = 0
        
        

    def next(self, val: int) -> float:
        
        self.q.append(val)
        self.total +=val
        
        if len(self.q) > self.maxsize:
            popped = self.q.popleft()
            self.total -= popped
        
        
        return self.total/len(self.q)
            
    
        
        
        
        
            
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)