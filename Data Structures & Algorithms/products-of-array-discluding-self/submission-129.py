class Solution:
    def productExceptSelf(self, nums):
        p = len(nums)
        res = [0] * p
        for i in range(p):
            prod = 1
            for j in range(p):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res