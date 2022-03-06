class Solution:
    def __init__(self):
        self.arr = []
        self.dic = {}
        self.count = []

    def subdomainVisits(self, cpdomains):
        sum_array = [0]
        ans = []
        for i in cpdomains:
            a = i.split(" ")
            self.merge(a[1], int(a[0]))
        for j in self.count:
            sum_array.append(j + sum_array[-1])

        for index, k in enumerate(sum_array[1:len(self.arr) + 1]):
            ans.append(str(k) + " " + self.arr[index])
        return ans

    def merge(self, string, num):
        b = string.split(".")
        for index in range(0, len(b)):
            s = ".".join(b[index:])
            if s not in self.dic:
                self.dic[s] = len(self.arr)
                self.arr.append(s)
                if len(self.arr) > len(self.count):
                    self.count.append(num)
                else:
                    self.count[self.dic[s]] += num
                self.count.append(-1 * num)
            else:
                self.count[self.dic[s]] += num
                self.count[self.dic[s] + 1] -= num

