class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            ans = max(ans, h * w)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans
