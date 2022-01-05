class Solution:
    def defangIPaddr(self, address: str) -> str: 
        result = ""
        
        for letter in address:
            if(letter=="."):
                result += "[.]"
            else:
                result += letter

        return result
        