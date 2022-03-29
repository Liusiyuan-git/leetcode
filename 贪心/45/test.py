class Solution:
    def jump(self, nums) -> int:
        now = ans = 0
        while now < len(nums) - 1:
            right = now + nums[now]
            if right >= len(nums) - 1:
                return ans + 1
            nextRight = right
            nextl = now
            for i in range(now+1,right+1):
                if i + nums[i] > nextRight:
                    nextRight = i + nums[i]
                    nextl =i
            now = nextl
            ans += 1
        return ans



