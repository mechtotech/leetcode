class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied+=customers[i]
                
        
        unsatisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                unsatisfied+=customers[i]
                
        maxunsatisfied = unsatisfied
       
    
        
        for i in range(minutes,len(customers)):
            if grumpy[i] == 1:
                unsatisfied+= customers[i]
            
            if grumpy[i-minutes] == 1:
                unsatisfied-= customers[i-minutes]
            maxunsatisfied = max(maxunsatisfied,unsatisfied)
        return maxunsatisfied + satisfied
                
        
        
        
        