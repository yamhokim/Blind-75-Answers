class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            while start < end:
                curr_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                if curr_sum < 0:
                    start += 1
                elif curr_sum > 0:
                    end -= 1
                else:
                    res.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                    start += 1

                    while sorted_nums[start] == sorted_nums[start - 1] and start < end:
                        start += 1
            
        return res