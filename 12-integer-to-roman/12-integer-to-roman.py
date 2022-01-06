class Solution:
    integer_numbers = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10: "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M",
    }
    
    def intToRoman(self, num: int) -> str:
        result = ""
        
        while(num):
            max_key = 0
            for key in self.integer_numbers:
                if (key <= num):
                    max_key = key
                else:
                    break;

            result += self.integer_numbers[max_key]
            num -= max_key
            
        return result
    