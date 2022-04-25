class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1, n):
                    digits[j] = 0
                return digits
        ans = [0] * (n + 1)
        ans[0] = 1
        return ans