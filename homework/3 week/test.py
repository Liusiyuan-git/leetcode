class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        to = [[] for i in range(numCourses)]  # 定义图
        inDeg = [0] * numCourses  # 定义节点入度数组
        for i in prerequisites:  # 构件图与入度数组
            x = i[0]
            y = i[1]
            to[y].append(x)
            inDeg[x] += 1
        queue = []  # 广搜 BFS queue
        lesson = []  # 存储已经修过的课程
        for i in range(0, numCourses):  # 入度为0的课程,适合做先修课程
            if inDeg[i] == 0:
                queue.append(i)
        while queue:
            q = queue[0]  # 取队列第一个课程
            queue = queue[1:]  # 队列出队
            lesson.append(q)  # 记录该课程，表明已经修过
            for i in to[q]:
                inDeg[i] -= 1  # 将修课程入度-1，当为0时，表明先修课程已经修完，该课程可以修，入队
                if inDeg[i] == 0:
                    queue.append(i)
        for i in inDeg:  # 如果入度数组里面有课程的度不是0，说明出现了环，死锁了
            if i != 0:
                return []
        return lesson  # 一切顺利，返回课程列表
