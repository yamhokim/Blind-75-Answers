class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_max = nums[0]
        global_max = nums[0]

        i = 1
        while i < len(nums):
            running_max = max(nums[i], running_max + nums[i])
            global_max = max(global_max, running_max)
            i += 1

        return global_max