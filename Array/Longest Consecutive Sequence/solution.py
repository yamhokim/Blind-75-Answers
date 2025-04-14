class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        visited = set()
        max_counter = 0

        for num in nums:
            if num - 1 in unique_nums or num in visited:
                continue
            else:
                counter = 1
                current_num = num
                while current_num + 1 in unique_nums:
                    counter += 1
                    current_num += 1

                max_counter = max(max_counter, counter)
            visited.add(num)

        return max_counter