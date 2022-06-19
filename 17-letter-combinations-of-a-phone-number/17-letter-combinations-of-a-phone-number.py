class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        
        def helper(s,i,slate):
            
            if i == len(s):
                if len(slate) >0:
                    result.append("".join(slate))
                return
            
            for pick in letters[s[i]]:
                slate.append(pick)
                helper(s,i+1,slate)
                slate.pop()
        helper(digits,0,[])
        return result
            
            
                
        
        
        