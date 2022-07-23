class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        m={}
        
        for i in dominoes:
            if tuple(sorted(i)) in m:
                m[tuple(sorted(i))] += 1
            else:
                m[tuple(sorted(i))] = 1
       
        count = 0
        for i in m.values():
            if i > 1:
                count+= comb(i,2)
        return count
            
            
        
        