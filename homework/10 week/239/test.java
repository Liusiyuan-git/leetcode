public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];
        TreeMap<Integer, Integer> tree = new TreeMap<>(); // treemap中存放的key为nums[i]，value为该值的计数
        // 将第1个窗口内的元素添加到tree中
        for (int i = 0; i < k; i++) {
            if (tree.containsKey(nums[i])) {
                tree.put(nums[i], tree.get(nums[i]) + 1);
            } else {
                tree.put(nums[i], 1);
            }
        }
        ans[0] = tree.lastKey(); // 获取最大值
        // 移动滑动窗口，在移动过程中中添加、删除元素，提取最大值放入结果数组
        for (int i = k; i < nums.length; i++) {
            // 添加新元素
            if (tree.containsKey(nums[i])) {
                tree.put(nums[i], tree.get(nums[i]) + 1);
            } else {
                tree.put(nums[i], 1);
            }
            // 删除旧元素
            int oldCount = tree.get(nums[i - k]);
            if (oldCount == 1) {
                tree.remove(nums[i - k]);
            } else {
                tree.put(nums[i - k], oldCount - 1);
            }
            ans[i - k + 1] = tree.lastKey();
        }
        return ans;
    }
}