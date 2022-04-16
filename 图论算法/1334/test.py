class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        d = [[1e9 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for i in edges:
            x = i[0]
            y = i[1]
            z = i[2]
            d[x][y] = z
            d[y][x] = z
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        minNeighbour = 1e9
        ans = 0
        for i in range(n):
            neighbour = 0
            for j in range(n):
                if i != j and d[i][j] <= distanceThreshold:
                    neighbour += 1
            if neighbour < minNeighbour or neighbour == minNeighbour and i > ans:
                minNeighbour = neighbour
                ans = i
        return ans
