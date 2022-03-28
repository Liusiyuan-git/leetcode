class Solution:
    def findContentChildren(self, g, s) -> int:
        ans = 0
        g.sort()
        s.sort()
        j = 0
        for child in g:
            while j < len(s) and s[j] < child:
                j += 1
            if j < len(s):
                ans += 1
                j += 1
        return ans

