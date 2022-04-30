class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        rightnost = 0
        for i in range(0, n):
            if i <= rightnost:
                rightnost = max(rightnost, i + nums[i])
                if rightnost >= n - 1:
                    return True
        return False
