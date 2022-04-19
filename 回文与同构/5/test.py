class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ansLen = 0
        ansStart = 0
        for center in range(0, n):
            l = center - 1
            r = center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ansLen:
                ansLen = r - l - 1
                ansStart = l + 1

        for center in range(1, n):
            l = center - 1
            r = center
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ansLen:
                ansLen = r - l - 1
                ansStart = l + 1
        print(ansStart, ansLen)
        return s[ansStart:ansStart + ansLen]
