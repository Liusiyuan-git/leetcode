class Solution:
    def groupAnagrams(self, strs):
        obs = {}
        for i in strs:
            calc = self.calcHash(i)
            if calc not in obs:
                obs[calc] = [i]
            else:
                obs[calc].append(i)
        return list(obs.values())


    def calcHash(self,string):
        string = list(string)
        string.sort()
        return "".join(string)