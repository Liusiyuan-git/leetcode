class Solution:
    def subdomainVisits(self, cpdomains):
        hashMap = {}
        ans = []
        for i in cpdomains:
            box = i.split(" ")
            count = int(box[0])
            dns = box[1].split(".")
            s = ""
            for j in range(len(dns)-1, -1, -1):
                s = dns[j] + "." + s
                c = s[:-1]
                if c not in hashMap:
                    hashMap[c] = count
                else:
                    hashMap[c] += count
        for i in hashMap.keys():
            ans.append(str(hashMap[i]) + " " + i)
        return ans