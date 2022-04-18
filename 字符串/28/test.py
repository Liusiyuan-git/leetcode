class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        b = 131
        p = int(1e9) + 7
        n = len(haystack)
        m = len(needle)
        H = [0] * (n + 1)
        for i in range(1, n + 1):
            H[i] = (H[i - 1] * b + (ord(haystack[i - 1]) - ord("a") + 1)) % p
        Hneedle = 0
        powPM = 1
        for ch in needle:
            Hneedle = (Hneedle * b + (ord(ch) - ord("a") + 1)) % p
            powPM = (powPM * b) % p
        for l in range(1, n - m + 2):
            r = l + m - 1
            if ((H[r] - H[l - 1] * powPM) % p + p) % p == Hneedle:
                return l - 1
        return -1
