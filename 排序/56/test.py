class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = [intervals[0]]
        for i in range(len(intervals)):
            if i > 0:
                interval = intervals[i]
                s = stack[-1]
                if interval[1] <= s[1]:
                    pass
                else:
                    if interval[0] <= s[1]:
                        stack.pop()
                        stack.append([s[0], interval[1]])
                    else:
                        stack.append(interval)
        return stack