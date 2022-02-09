class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        for r in range(0, n):
            for c in range(0, n):
                new_value = min([max(grid[r]), max([grid[x][c] for x in range(0, n)])])
                result += new_value - grid[r][c]
                grid[r][c] =  new_value
                
        return result
        
        