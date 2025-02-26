class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            compliment_value = target - nums[i]
            if compliment_value in pairs:
                return [pairs[compliment_value], i]
            else:
                pairs[nums[i]] = i