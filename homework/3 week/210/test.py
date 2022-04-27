class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        ans = []
        d = [0] * numCourses
        mp = [[] for _ in range(numCourses)]
        for i in prerequisites:
            mp[i[1]].append(i[0])
            d[i[0]] += 1
        queue = []
        for i in range(numCourses):
            if d[i] == 0:
                queue.append(i)
        while queue:
            c = queue[0]
            ans.append(c)
            queue = queue[1:]
            for i in mp[c]:
                d[i] -= 1
                if d[i] == 0:
                    queue.append(i)
        if len(ans) != numCourses:
            return []
        return ans