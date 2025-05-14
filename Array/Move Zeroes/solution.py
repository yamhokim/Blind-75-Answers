class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Keep a value that keeps track of the index the next non-zero value will go to
        swapIndex = 0

        # Iterate through the array of numbers
        for i in range(len(nums)):
            # If the current value we're looking at is non-zero, perform a swap and increment the swapIndex
            if nums[i] != 0:
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                swapIndex += 1
            
        