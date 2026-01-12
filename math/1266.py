class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range (1, len(points)):
            prev = points[i-1]
            curr = points[i]
            diff1 = abs(curr[0] - prev[0])
            diff2 = abs(curr[1] - prev[1])
            time += max(diff1, diff2)
        return time
