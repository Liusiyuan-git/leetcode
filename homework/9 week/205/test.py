class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        use = {}
        for i in range(len(s)):
            if t[i] not in use and s[i] not in dic:  # 没映射，加入map
                dic[s[i]] = t[i]
                use[t[i]] = 1
            elif t[i] not in use and s[i] in dic:  # 不符合：相同字符只能映射到同一个字符上 这一条件
                return False
            elif t[i] in use and s[i] not in dic:  # 不符合：不同字符不能映射到同一个字符上 这一条件
                return False
            else:
                if dic[s[i]] != t[i]:  # 不符合：相同字符只能映射到同一个字符上 这一条件
                    return False
        return True
