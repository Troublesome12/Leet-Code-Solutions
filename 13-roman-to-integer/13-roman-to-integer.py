class Solution:
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    def romanToInt(self, s: str) -> int:
        value = 0
        
        while(s):
            if s[:2] in self.roman_numbers:
                value += self.roman_numbers[s[:2]]
                s = s[2:]
                
            elif s[:1] in self.roman_numbers:
                value += self.roman_numbers[s[:1]]
                s = s[1:]
                
            
                
        return value