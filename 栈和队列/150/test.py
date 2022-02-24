class Solution:
    def largestRectangleArea(self, heights) -> int:
        location = [0]
        stack = [heights[0]]
        maxArea = heights[0]
        for index, i in enumerate(heights):
            if index > 0:
                if i < stack[-1]:
                    while stack and stack[-1] > i:
                        instance = index - location[-1]
                        area1 = instance * stack[-1]
                        area2 = i * (instance + 1)
                        maxArea = max(maxArea, area1, area2)
                        stack.pop()
                        location.pop()
                stack.append(i)
                location.append(index)
        if stack:
            instance = location[-1]
            for i in range(len(location) - 1, -1, -1):
                area = (instance - location[i] + 1) * stack[i]
                maxArea = max(maxArea, area)
        return maxArea


s = Solution()
s.largestRectangleArea([9, 8, 7, 6, 5, 4, 3, 2, 1])
