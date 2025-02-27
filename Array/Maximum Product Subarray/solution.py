class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        running_max = nums[0]
        running_min = nums[0]
        global_max = nums[0]

        i = 1
        while i < len(nums):
            temp_running_max = running_max
            running_max = max(nums[i], running_max * nums[i], running_min * nums[i])
            running_min = min(nums[i], running_min * nums[i], temp_running_max * nums[i])
            global_max = max(global_max, running_max)

            i += 1

        return global_max