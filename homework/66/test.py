class Solution:
    def plusOne(self, digits):
        result = []
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            count = digits[i] + add
            if count >= 10:
                add = 1
                result = [count - 10] + result
            else:
                add = 0
                result = [count] + result
        if add:
            result = [1] + result
        return result
