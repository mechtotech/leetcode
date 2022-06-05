class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        b =sorted(boxTypes,key=lambda x:x[1],reverse =True)
        
        units = 0
        for i in range(len(b)):
            if truckSize >= 0:
                boxcount=min(truckSize,b[i][0])
                units+=boxcount*b[i][1]
                truckSize-=boxcount
                if truckSize == 0:
                    break
                
        
        return units
                
                
            
        
            
        
        