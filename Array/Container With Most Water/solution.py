class Solution:
    def maxArea(self, height: List[int]) -> int:
        running_max = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            running_max = max(area, running_max)

            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1

        return running_max