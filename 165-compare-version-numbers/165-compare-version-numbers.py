class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        n1= len(version1)
        n2 = len(version2)
        n = n1
        
        
        # append zero to smaller version
        if n1>n2:
            version2+= ['0']*(n1-n2)
            n= n1
        if n2 >n1:
            version1 +=['0']*(n2-n1)
            n=n2
            
            
        i = 0
        j = 0
        
        while i < n and j < n:
            if int(version1[i]) > int(version2[j]):
                return 1
            elif int(version1[i]) < int(version2[j]):
                return -1
            else:
                i += 1
                j += 1
                
            
        return 0
        
        
        
    
       
    
            
        
        
        
        
        