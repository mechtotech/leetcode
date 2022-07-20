from random import choice
class RandomizedSet:

    def __init__(self):
        self.m={}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        else:
            self.m[val] = len(self.list)
            self.list.append(val)
            return True
            
        
    def remove(self, val: int) -> bool:
        if val in self.m:
            self.m[self.list[-1]]=self.m[val] 
            self.list[self.m[val]],self.list[-1]=self.list[-1],self.list[self.m[val]]
             
            self.list.pop()
            del self.m[val]
            return True
        else:
            return False
            
            

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()