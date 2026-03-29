class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0] * n
        for y in range(n):
            prod = 1
            for w in range(n):
                if y == w:
                    continue
                prod *= nums[w]
            res[y] = prod
        return res