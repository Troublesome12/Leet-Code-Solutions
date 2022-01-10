class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        length = len(boxes)
        answer = []
        # for i in range(length):
        #     answer.append(0)
        

        for i in range(length):
            count = 0
            for j in range(length):
                if i == j:
                    continue
                    
                if boxes[j] == '0':
                    continue
                else:
                    count += abs(j-i)
                    
            answer.append(count)
            
        return answer
                    
                    
                