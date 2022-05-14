class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_len = len(s)
        for i in range(s_len):
            have_found = False
            
            for j in range(s_len):
                
                if i == j:
                    continue
                
                if s[i] == s[j]:
                    have_found = True
                    break
                
                
            if not have_found:
                return i
            
        return -1
                
        