class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        for ch in s:
            if ch >= "0" and ch <= "9" or ch >= "a" and ch <= "z":
                t.append(ch)
            if ch >= "A" and ch <= "Z":
                t.append(ch.lower())
        left = 0
        right = len(t) - 1
        while left < right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        return True
