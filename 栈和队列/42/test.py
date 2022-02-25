class Solution:
    def trap(self, heights) -> int:
        ans = 0
        stack = []
        for height in heights:
            accumulateWidth = 0
            while stack and stack[-1]["height"] <= height:
                bottom = stack[-1]["height"]
                accumulateWidth += stack[-1]["width"]
                stack.pop()
                if not stack:
                    up = 0
                    continue
                else:
                    up = min(height, stack[-1]["height"])

                ans += accumulateWidth * (up - bottom)
            stack.append({"width": accumulateWidth + 1, "height": height})
        return ans

#法二
    def trap(self, heights) -> int:
        ans = 0
        n = len(heights)
        preMax = [0] * n
        surfMax = [0] * n
        preMax[0] = heights[0]
        surfMax[n - 1] = heights[n - 1]
        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], heights[i])

        for i in range(n - 2, -1, -1):
            surfMax[i] = max(surfMax[i + 1], heights[i])

        for i in range(1, n - 1):
            up = min(preMax[i - 1], surfMax[i + 1])
            bottom = heights[i]
            if up > bottom:
                ans += up - bottom
        return ans
