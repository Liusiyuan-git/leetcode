class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        count = [0] * 30
        for i in range(n):
            l = ord(s[i]) - ord("a")
            count[l] += 1

        vis = [False] * 30
        ans = []
        for i in range(n):
            cl = ord(s[i]) - ord("a")
            if not vis[cl]:
                while ans and count[ord(ans[-1]) - ord("a")] > 0 and ans[-1] > s[i]:
                    vis[ord(ans[-1]) - ord("a")] = False
                    ans.pop()
                vis[cl] = True
                ans.append(s[i])
            count[cl] -= 1
        return "".join(ans)
