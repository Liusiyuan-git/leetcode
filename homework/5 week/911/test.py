class TopVotedCandidate:

    def __init__(self, persons, times):
        self.times = times
        self.tops = []
        voteMap = {-1: -1}
        top = -1
        for i in persons:
            if i not in voteMap:
                voteMap[i] = 1
            else:
                voteMap[i] += 1
            if voteMap[i] >= voteMap[top]:
                top = i
            self.tops.append(top)

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.tops[left]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
