class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum < target:
                start += 1
            elif curr_sum > target:
                end -= 1
            else:
                return [start + 1, end + 1]
        