class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        f(n) = maximum profit on the nth day
        f(n) = min(price[n])
        
        """
        
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit+=prices[i]-prices[i-1]
        
        return maxprofit
        
        