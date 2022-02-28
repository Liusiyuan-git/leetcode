class Solution:
    def robotSim(self, commands, obstacles) -> int:
        obs = {}
        for i in obstacles:
            obs[self.calcHash(i)] = 1
        x = y = 0
        dir = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        ans = 0
        for command in commands:
            if command == -1:
                dir = (dir + 1) % 4
            elif command == -2:
                dir = (dir + 3) % 4
            else:
                for i in range(0, command):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if self.calcHash([nx, ny]) in obs:
                        break
                    x = nx
                    y = ny
                    ans = max(ans, x ** 2 + y ** 2)
        return ans

    def calcHash(self, obstacle):
        return str(obstacle[0]) + "," + str(obstacle[1])
