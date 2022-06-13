class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        k = len(p)
        m_p ={}
        m_s = {}
        
        output = []
        
        for i in range(k):
            if p[i] in m_p:
                m_p[p[i]]+=1
            else:
                m_p[p[i]] = 1
        for i in range(k):
            if s[i] in m_s:
                m_s[s[i]]+=1
            else:
                m_s[s[i]] = 1
        
        if m_p == m_s:
            output.append(0)
        
        for i in range(k,len(s)):
            if s[i] in m_s:
                m_s[s[i]]+=1
            else:
                m_s[s[i]] = 1
            m_s[s[i-k]] -= 1
            if m_s[s[i-k]] == 0:
                del m_s[s[i-k]]
            if m_p == m_s:
                output.append(i-k+1)
        return output
            
            
            
            
        
            
            
        
        
        