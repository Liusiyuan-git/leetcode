class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        sign = 1
        if index < len(s):
            if s[index] == "+":
                index += 1
            elif s[index] == "-":
                sign = -1
                index += 1
        val = 0
        while index < len(s) and s[index] >= "0" and s[index] <= "9":
            val = val * 10 + ord(s[index]) - ord("0")
            if val > 2147483647:
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
            index += 1
        return val * sign


s = Solution()
s.myAtoi("+-12")
