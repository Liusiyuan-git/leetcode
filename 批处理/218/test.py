import heapq


class Solution:
    def getSkyline(self, buildings):
        n = len(buildings)
        events = []
        removed = [False] * n
        for i in range(n):
            left = buildings[i][0]
            right = buildings[i][1]
            height = buildings[i][2]
            events.append([left, height, 1, i])
            events.append([right, height, -1, i])
        events = sorted(events, key=lambda x: x[0])
        queue = []
        ans = []
        for i in range(len(events)):
            if events[i][2] == 1:
                heapq.heappush(queue, (-events[i][1], events[i][3]))
            else:
                removed[events[i][3]] = True

            if i == len(events) - 1 or events[i][0] != events[i + 1][0]:
                while queue and removed[heapq.nsmallest(1, queue)[0][1]]:
                    heapq.heappop(queue)
                height = 0
                if queue:
                    height = -heapq.nsmallest(1, queue)[0][0]
                if not ans or height != ans[-1][1]:
                    ans.append([events[i][0], height])
        return ans
