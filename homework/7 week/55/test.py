class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        nums = [0] + nums
        f = [False] * (n + 1)  # f[i] 表示能否跳到以i为下标的这个点
        f[1] = True  # 默认第一个开始，所以第一个肯定是可以的
        i = 1
        while i <= n:  # 数组跑一边，每个都遍历，从1开始
            instant = i  # 记录最远距离
            dic = {}  # 记录最远距离与下标的映射
            for j in range(0, nums[i] + 1):  # 最大跳跃 nums[i]，最小不跳跃，为0
                if i + j <= n:  # 不允许跳过界
                    f[i + j] = f[i]  # i + j 是可以通过 i 跳跃 j 到达的，为True
                    far = i + j + nums[i + j]  # 往后看两步，取最远距离比较
                    if far >= n:  # 最远距离不允许过界
                        far = n
                    dic[far] = i + j  # 记录最远距离与下标的映射
                    instant = max(instant, far)  # 记录最远距离
            if instant == i:  # 如果最远距离跟当前下标一样，说明要么跳不动，本身就是0，要么到边界了，需要往前移动一步进而继续计算或者结束循环
                i += 1
            else:
                i = dic[instant]  # 下一跳，从两步后可以跳到最远距离的点开始
        return f[n]
