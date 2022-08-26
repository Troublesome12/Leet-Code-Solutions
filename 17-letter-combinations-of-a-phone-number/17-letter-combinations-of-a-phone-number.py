class Solution:
    keyboard = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        
    def build_combination(self, list1: List[str], list2: List[str]) -> List[str]:
        result_list = []

        for x in list1:
            for y in list2:
                result_list.append(x+y)

        return result_list
    
    def letterCombinations(self, digits: str) -> List[str]:
        digits_length = len(digits)
        if not digits_length:
            return []
        
        elif digits_length == 1:
            return self.keyboard[digits]
    
        result_conbinations = self.keyboard[digits[0]]
        for index in range(1, digits_length):
            result_conbinations = self.build_combination(result_conbinations,       self.keyboard[digits[index]])

        return result_conbinations
        
        