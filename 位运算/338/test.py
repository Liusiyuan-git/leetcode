class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0] * (n + 1)
        for i in range(1, n+1):
            cnt[i] = cnt[i & (i-1)] + 1
        return cnt