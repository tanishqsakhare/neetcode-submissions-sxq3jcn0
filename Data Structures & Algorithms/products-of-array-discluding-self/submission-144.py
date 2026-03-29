class Solution:
    def productExceptSelf(self, nums):
        b = len(nums)
        res = [0] * b
        for i in range(b):
            prod = 1
            for j in range(b):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res