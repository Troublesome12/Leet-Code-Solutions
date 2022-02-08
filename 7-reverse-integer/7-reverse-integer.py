class Solution:
    def reverse(self, x: int) -> int:
        result = []
        if x < 0:
            result.append('-')
            x = abs(x)
        
        x = list(str(x))
        while len(x) > 1 and x[len(x)-1] == '0':
            x.pop()

        for index in range(len(x)-1, -1, -1):
            result.append(x[index])
        
        result = "".join(result)
        if int(result) < -2147483647 or int(result) > 2147483647:
            return 0
        return result
