class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.n = {}
        self.activity = 0
        
        

    def get(self, key: int) -> int:
        
        if key in self.m:
            self.activity +=1
            self.n[key] = self.activity
            return self.m[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.m:
            self.activity +=1
            self.n[key] = self.activity
            self.m[key]= value
        else:
            if len(self.m)< self.capacity:
                self.activity +=1
                self.n[key] = self.activity
                self.m[key]= value
                
            else:
                self.activity +=1
                self.n[key] = self.activity
                self.m.pop(min(self.n, key=self.n.get))
                self.n.pop(min(self.n, key=self.n.get))
                self.m[key] = value
                
        
                
                
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)