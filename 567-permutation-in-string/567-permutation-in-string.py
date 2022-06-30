class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        m_s1 = {}
        m_s2 = {}
        
        for i in range(k):
            if s1[i] in m_s1:
                m_s1[s1[i]] +=1
            else:
                m_s1[s1[i]] = 1
    
        for i in range(k):
            if s2[i] in m_s2:
                m_s2[s2[i]] +=1
            else:
                m_s2[s2[i]] =1
        
        if m_s1 == m_s2:
            return True
        
        
        for i in range(k,len(s2)):
            if s2[i] in m_s2:
                m_s2[s2[i]] +=1
            else:
                m_s2[s2[i]] = 1
            m_s2[s2[i-k]]-=1
            if m_s2[s2[i-k]] == 0:
                
                del m_s2[s2[i-k]] 
            
            if m_s2 == m_s1:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
    

            
            