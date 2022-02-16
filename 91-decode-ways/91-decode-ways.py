class Solution:
    def numDecodings(self, s: str) -> int:
        
        '''
        f(n) = # no. of ways to decode the string of length 0...n
        
        f(n) = f(n-1) valid only if s[n-1] !="0"   
                         +
             
               f(n-2) if s[n-2] is either "1" or "2" and if "2" then s[n-1] should be b/w "0..6"
        
         
        base case 
        
        f(0) # zero prefix = 1
        
        f(1) =  0 if s[0]==0 else 0
        
        
        
        '''
        n= len(s)
        DP = [0 for i in range(n+1)]
        DP[0] = 1 
        if s[0] == "0":
            DP[1] = 0
        else:
            DP[1]=1
        
        for i in range(2,n+1):
            DP[i] = 0
            if s[i-1] != "0":
        
                DP[i] +=DP[i-1]
            
            if s[i-2] =="1" or (s[i-2]=="2" and s[i-1] in ["1","2","3","4","5","6","0"]):
                DP[i] +=DP[i-2]
        
        return DP[n]
            
                
            
            
            
        
        