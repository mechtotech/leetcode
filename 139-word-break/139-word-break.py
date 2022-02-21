class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        DP = [False for i in range(len(s)+1)]
        
        DP[0] = True
        
        for i in range (1,len(s)+1):
            for lastwordlen in range(0,i):
                
                if s[lastwordlen:i] in wordDict and DP[lastwordlen] is True:
                    
                    DP[i]  = True
                    break
                
        
        return DP[-1]
        
        
        
        