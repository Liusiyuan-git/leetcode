class Solution:
    def minimumEffort(self, tasks) -> int:
        tasks = sorted(tasks,key=lambda x:x[0]-x[1])
        ans = 0
        tasks.reverse()
        for i in tasks:
            ans = max(i[1],ans+i[0])
        return ans