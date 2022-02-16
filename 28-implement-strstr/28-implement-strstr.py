class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_l, needle_l = len(haystack), len(needle)
        if needle_l == 0:
            return 0
        
        if haystack_l < needle_l:
            return -1
        
        for i in range(haystack_l):
            if haystack[i] == needle[0]:
                subHaystack = haystack[i:i+needle_l]
                if subHaystack == needle:
                    return i
            
        return -1
                
                
                
                
                
                
            
            