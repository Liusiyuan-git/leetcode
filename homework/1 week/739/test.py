class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                l = stack[-1]
                ans[l] = i - stack.pop()
            stack.append(i)
        return ans