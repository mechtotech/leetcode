class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        1 2     n  
        _ _ _ _ _ 
            j    n-1
        
        '''
        result = []
        
        n = len(arr)
        for i in range(n-1,-1,-1):
            if arr[i] !=i+1:
                for j in range(i-1,-1,-1):
                    if arr[j] == i+1:
                        break
                
                arr[:j+1] = arr[:j+1][::-1]
                arr[:i+1] = arr[:i+1][::-1]
                result.append(j+1)
                result.append(i+1)
        
        return result
                
            
        
        
        
        