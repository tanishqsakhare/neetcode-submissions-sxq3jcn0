class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0] * n
        for x in range(n):
            prod = 1
            for z in range(n):
                if x == z:
                    continue
                prod *= nums[z]
            res[x] = prod
        return res