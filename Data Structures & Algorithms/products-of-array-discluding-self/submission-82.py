class Solution:
    def productExceptSelf(self, nums):
        res = [0] * len(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res