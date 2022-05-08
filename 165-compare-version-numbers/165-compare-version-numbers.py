class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #1. split the original string by .
        version1 = version1.split('.') 
        version2 = version2.split('.')
        
        n1 = len(version1)
        n2 = len(version2)
        n = n1
        
        #2. append '0' to the shorter list if there is one
        if n1 > n2:
            version2 += ['0'] * (n1-n2)
            n = n1
            
        if n1 < n2:
            version1 += ['0'] * (n2-n1)
            n = n2


        #3. use two pointers to walk through 
        # the two list and compare
        # one by one position   
        pt1 = 0
        pt2 = 0
        
        while pt1 < n and pt2 < n:
            if int(version1[pt1]) > int(version2[pt2]):
                return 1
            elif int(version1[pt1]) < int(version2[pt2]):
                return -1
            else:
                pt1 += 1
                pt2 += 1
                
            
        return 0
        
        
        
        