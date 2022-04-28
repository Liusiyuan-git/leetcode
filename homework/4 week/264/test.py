import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2,3,5]
        seen = set()
        heap = []
        seen.add(1)
        heapq.heappush(heap, 1)
        ugly = 0
        for i in range(n):
            curr = heapq.heappop(heap)
            ugly = curr
            for factor in factors:
                value = curr * factor
                if value not in seen:
                    seen.add(value)
                    heapq.heappush(heap, value)
        return ugly