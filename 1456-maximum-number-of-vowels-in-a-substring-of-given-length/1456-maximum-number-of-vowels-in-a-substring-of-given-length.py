class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a':1,'e':1,'i':1,'o':1,'u':1}
        
        countvowels = 0
        
        for i in range(k):
            if s[i] in vowels:
                countvowels +=1
        
        maxvowel = countvowels
        for i in range(k,len(s)):
            if s[i] in vowels:
                countvowels +=1
            if s[i-k] in vowels:
                countvowels-=1
            maxvowel= max(countvowels,maxvowel)
        return maxvowel
    
        
                
        
                
            
        
        
        