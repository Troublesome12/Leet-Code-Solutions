class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digit_len = len(digits)
        
        for i in range(digit_len-1, -1, -1):
            temp = digits[i] + 1
        
            if temp <= 9:
                digits[i] = temp
                return digits
        
            digits[i] = 0          
            
        
        result = [1]
        return result + digits
        