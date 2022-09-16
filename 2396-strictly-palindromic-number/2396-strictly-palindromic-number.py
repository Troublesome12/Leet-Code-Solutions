class Solution:
    
    def convert_base(self, value, base):
        s = ''
        while value != 0:
            s = str(value%base) + s
            value = value//base
        
        return int(s)
    
    
    def is_palindrom(self, value):
        value = str(value)
        rev_value = value[::-1]
        
        if value == rev_value:
            return True
        
        return False
        
    
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for base in range(2, n-1):
            value = self.convert_base(n, base)
            if not self.is_palindrom(value):
                return False
            
        return True