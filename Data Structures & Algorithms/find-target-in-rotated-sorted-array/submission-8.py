class Solution:
    def search(self, nums, target):
        for p in range(len(nums)):
            if nums[p] == target:
                return p

        return -1