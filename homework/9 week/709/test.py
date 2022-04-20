class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in s:
            if i >= "A" and i <= "Z":
                ans += chr(ord(i) - ord("A") + ord("a")) # 大写转小写
            else:
                ans += i
        return ans
