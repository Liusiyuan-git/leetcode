class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            need = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            if need <= days:
                right = mid
            else:
                left = mid + 1
        return left
