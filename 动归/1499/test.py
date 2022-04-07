class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        q = []
        ans = -1e9
        for i in range(0, len(points)):
            while q and points[q[0]][0] < points[i][0] - k:
                q = q[1:]
            if q:
                ans = max(ans, points[i][0] + points[i][1] + points[q[0]][1] - points[q[0]][0])
            while q and points[q[-1]][1] - points[q[-1]][0] < points[i][1] - points[i][0]:
                q.pop()
            q.append(i)
        return ans