import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.caculate(piles, mid) > h:
                left = mid + 1
            else:
                right = mid
        return left
    def caculate(self, piles, mid):
        count = 0
        for pile in piles:
            count += math.ceil(pile / mid)
        return count