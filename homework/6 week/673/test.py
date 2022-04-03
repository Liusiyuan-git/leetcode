class Solution:
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        f = [1] * n  # f[i] 表示以i为结束的最长子序列长度
        fs = [1] * n  # fs[i] 表示以i为结束的最长子序列长度的数量
        dic = {1: 1}  # dic 用来统计整个数组最长子序列数量
        for i in range(1, n):
            store = {1: 1}  # store用来统计以i为结束的最长子序列的数量
            for j in range(i):
                if nums[i] > nums[j]:
                    if f[j] + 1 >= f[i]:  # 符合递增条件
                        f[i] = f[j] + 1
                        if f[i] not in store:  # 统计符合的子序列的数量
                            store[f[i]] = fs[j]
                        else:
                            store[f[i]] += fs[j]
            fs[i] = store[f[i]]  # 更新 fs
            if f[i] not in dic:  # 更新 dic
                dic[f[i]] = store[f[i]]
            else:
                dic[f[i]] += store[f[i]]
        return dic[max(f)]  # max取出子序列的最长长度，然后用该长度从dic取出对应数量
