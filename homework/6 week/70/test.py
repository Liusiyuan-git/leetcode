class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:  # 确定边界
            return 1
        arr = [1, 1]
        for i in range(2, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])  # 最优子结构，n为结束的楼梯，要么从 n-2 走两步上来， 要么从 n-1 走一步上来
        return arr[-1]
