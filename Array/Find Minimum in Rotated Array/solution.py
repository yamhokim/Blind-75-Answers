class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        running_min = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                running_min = min(running_min, nums[left])
                break

            middle = (left + right) // 2
            running_min = min(running_min, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return running_min