class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        
        
        intervals.sort()
        for i in range(len(intervals)):
            
            if len(merged) ==0 or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            
            elif merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(intervals[i][1],merged[-1][1])
                    
        
        return merged
        
        
        
        
        