class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        dist = [1e9] * (n + 1)
        dist[k] = 0
        for i in range(1, n):
            flag = False
            for j in times:
                x = j[0]
                y = j[1]
                z = j[2]
                if dist[y] > dist[x] + z:
                    dist[y] = dist[x] + z
                    flag = True
            if not flag:
                break
        ans = 0
        for i in dist[1:]:
            ans = max(ans, i)
        if ans == 1e9:
            return -1
        else:
            return ans