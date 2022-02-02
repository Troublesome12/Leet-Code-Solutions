class Solution:
    opening_operators = [ "{", "[", "("]
    closing_operators = [ "}", "]", ")"]
    
    def isMatched(self, opening: str, closing: str) -> bool:
        if  (opening == '(' and closing == ')') \
            or (opening == '{' and closing == '}') \
            or (opening == '[' and closing == ']'):
            return True
        return False
        
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in self.opening_operators:
                stack.append(x)
                
            elif x in self.closing_operators:
                if not len(stack):
                    return False
    
                if not self.isMatched(stack.pop(), x):
                    return False
        
        if not len(stack):
            return True
    
        return False
        
