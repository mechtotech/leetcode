class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        f(n) = number of distinct phone number of length n
        
        _ _ _ _ _ _
        1 2       n           
        
        n   n-1
        0   4,6
        1   6,8
        2- 7,9
        3 - 4,8
        4 - 3,9,0
        5 - any digit
        6-  0,1,7
        7- 9,2
        8- 1,3
        9 - 4,2
        
        f(length,last digit) = f(n,d) = # number of distinct phone numbers of length n with lastdigit d
         
         f(4,0) = f(3,4)+f(3,6)
         
         unique subptoblem 10*n
         space = 
         
         f(1,0)  f(2,0)  
         f(1,1)
         f(1,2)
         f(1,3)
         f(1,4)
         .
         .
         f(1,10)
         for row in range()
         DP[row][1] = 1
         n   n-1
        0   4,6
        1   6,8
        2- 7,9
        3 - 4,8
        4 - 3,9,0
        5 - any digit
        6-  0,1,7
        7- 9,2
        8- 1,3
        9 - 4,2
         
        '''
        DP = [[0 for i in range(10)] for j in range(n+1)]
        
        for col in range(10):
            DP[1][col] = 1
        
        
        for row in range(2,n+1):
            DP[row][0] = DP[row-1][4]+ DP[row-1][6]
            DP[row][1] = DP[row-1][8]+ DP[row-1][6]
            DP[row][2] = DP[row-1][7]+ DP[row-1][9]
            DP[row][3] = DP[row-1][4]+ DP[row-1][8]
            DP[row][4] = DP[row-1][3]+ DP[row-1][9] + DP[row-1][0]
            DP[row][5] = 0
            DP[row][6] = DP[row-1][1]+ DP[row-1][7] + DP[row-1][0]
            DP[row][7] = DP[row-1][6]+ DP[row-1][2]
            DP[row][8] = DP[row-1][1]+ DP[row-1][3]
            DP[row][9] =DP[row-1][4]+DP[row-1][2]
        
        
        return sum(DP[-1]) % ((10**9)+7 )
            
                
        
        
    
    
        
        
        
        