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
