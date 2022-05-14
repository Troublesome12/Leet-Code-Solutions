class Solution:
    def firstUniqChar(self, s: str) -> int:
        ordered_dict = dict()
        
        for char in s:
            if char in ordered_dict:
                ordered_dict[char] += 1
            else:
                ordered_dict[char] = 1

        for k, v in ordered_dict.items():
            if v == 1:
                return s.index(k)
        
        return -1
            
                
        