'''
Initial Approach - O(n) Time and O(n) Space
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 1
        
        for i in range(len(nums) + 1):
            if i not in nums_dict:
                return i

'''
XOR Approach - O(n) Time and O(1) Space
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num

        for i in range(len(nums) + 1):
            res = res ^ i
        
        return res
    
'''
Sum Difference Approach - O(n) Time and O(1) Space
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_sum = 0
        for i in range(len(nums) + 1):
            range_sum += i

        return range_sum - sum(nums)