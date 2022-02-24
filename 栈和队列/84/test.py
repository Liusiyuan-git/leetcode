class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights.append(0)
        s = []
        for height in heights:
            accumulatedWidth = 0
            while s and s[-1]["height"] >= height:
                accumulatedWidth += s[-1]["width"]
                ans = max(ans, s[-1]["height"] * accumulatedWidth)
                s.pop()
            s.append({"width": accumulatedWidth + 1, "height": height})
        return ans
