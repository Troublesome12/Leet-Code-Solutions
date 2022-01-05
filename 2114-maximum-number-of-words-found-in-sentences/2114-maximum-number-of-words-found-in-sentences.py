class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max = 1
        for sentance in sentences:
            count = 1
            
            for letter in sentance:
                if letter == ' ':
                    count+=1
            
            if count > max:
                max = count
        
        return max
        