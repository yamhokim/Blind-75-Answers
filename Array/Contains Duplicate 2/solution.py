class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        encountered_nums = {}

        for i in range(len(nums)):
            if nums[i] in encountered_nums and abs(i - encountered_nums[nums[i]]) <= k:
                return True
            else:
                encountered_nums[nums[i]] = i

        return False