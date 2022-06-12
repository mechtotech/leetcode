class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        window = sum(calories[:k])
        count = 0
        if window > upper:
            count+=1
        elif window < lower:
            count-=1
        
        for i in range(k,len(calories)):
            window += calories[i] - calories[i-k]
            if window > upper:
                count+=1
            elif window < lower:
                count-=1
        return count
            
        
        