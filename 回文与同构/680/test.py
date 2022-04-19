class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.check(s, 0, len(s) - 1, 1)

    def check(self, s, left, right, times):
        while left < right:
            if s[left] != s[right]:
                return times > 0 and (
                            self.check(s, left + 1, right, times - 1) or self.check(s, left, right - 1, times - 1))
            left += 1
            right -= 1
        return True
