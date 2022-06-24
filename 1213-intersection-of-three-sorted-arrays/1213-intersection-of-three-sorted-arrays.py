class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        i = 0
        j=0
        arr12=[]
        arr123=[]
        while i < len(arr1) and j < len(arr2):
            if arr1[i]==arr2[j]:
                arr12.append(arr1[i])
                i+=1
                j+=1
            
            elif arr1[i]<arr2[j]:
                i+=1
            
            else:
                j+=1
        
        while i < len(arr1):
            
            i+=1
        
        while j < len(arr2):
            
            j+=1
        
        a=0
        b=0
        
        while a < len(arr12) and b < len(arr3):
            
            if arr12[a]==arr3[b]:
                arr123.append(arr12[a])
                
                a+=1
                b+=1
            
            elif arr12[a]<arr3[b]:
                a+=1
            
            else:
                b+=1
        
        while a < len(arr12):
            a+=1
        
        while b < len(arr3):
            b+=1
        
        return arr123