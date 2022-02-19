class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        '''
        f(a) = # coins needed to make up the amount a from coins
        
             f(a-5)      f(a-2)         f(a-1)      f(a)
             
        f(a) = min(f(a-1),f(a-2),f(a-5)) +1
        
        '''
        
        DP = [None for i in range(amount+1)]
        DP[0] = 0
        for i in range(1,amount+1):
            minimum = float('inf')
            for c in coins:
                if i - c >= 0:
                    minimum = min(DP[i-c],minimum)
            
            DP[i] = minimum+1
        
        return DP[amount] if DP[amount] != float('inf') else -1
                
       
    
                    
        
        