class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        to = [[] for i in range(numCourses)]
        inDeg = [0] * numCourses
        for i in prerequisites:
            x = i[0]
            y = i[1]
            to[y].append(x)
            inDeg[x] += 1
        queue = []
        lesson = []
        for i in range(0, numCourses):
            if inDeg[i] == 0:
                queue.append(i)
        while not queue:
            q = queue[0]
            queue = queue[1:]
            lesson.append(q)
            for i in to[q]:
                inDeg[i] -= 1
                if inDeg[i] == 0:
                    queue.push(i)
        return len(lesson) == numCourses


s = Solution()
s.canFinish(2, [[1, 0]])
