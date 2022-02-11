class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        
        for i in range(len(encoded)):
            next_value = encoded[i] ^ result[i]
            result.append(next_value)
            
        return result