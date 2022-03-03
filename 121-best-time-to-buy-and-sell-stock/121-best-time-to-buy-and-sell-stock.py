class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        '''
        _ _ _ _ _  _
               n-2 n-1
        
        # to maximuize the sell price the selling price should be high
        # min element needs to be selected price[0...n-2]
               
        
        
        '''
        
        profit = 0
        prevmin= prices[0]
        n= len(prices)
        for i in range(1,n):
            profit = max(prices[i]-prevmin,profit)
            prevmin = min(prices[i],prevmin)
        
        return profit
        
        
    
        