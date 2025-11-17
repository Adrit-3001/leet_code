class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        i = 0
        most = 0
        while n - i > 0:
            if most < min(height[i], height[n])*(n-i):
                most = min(height[i], height[n])*(n-i)
            if max(height[i], height[n]) == height[n]:
                i += 1
            else:
                n -= 1
        return most
