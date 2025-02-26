class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encountered_nums ={}
        for num in nums:
            if num in encountered_nums:
                return True
            else:
                encountered_nums[num] = 1
        
        return False