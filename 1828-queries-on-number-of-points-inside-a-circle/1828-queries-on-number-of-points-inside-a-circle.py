class Solution:
    def countPointsOnCircle(self, points: List[List[int]], circle: List[int]) -> int:
        count = 0
        for point in points:
            if (point[0]-circle[0])**2 + (point[1]-circle[1])**2 <= (circle[2])**2:
                count += 1
        
        return count
        
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            answer.append(self.countPointsOnCircle(points, query))
        
        return answer