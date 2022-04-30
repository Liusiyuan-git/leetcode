class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        ans = 0
        for i in range(32):
            ans = ans << 1 | (n >> i & 1)
        return ans