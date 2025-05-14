class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Start by declaring the borders/boundaries
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            for i in range(right - left):
                top, bot = left, right  # We're able to do this since we're dealing with a square matrix

                # Store the top right value
                top_right = matrix[top + i][right]

                # Move the top left value into the top right position
                matrix[top + i][right] = matrix[top][left + i]

                # Store the bottom right value
                bot_right = matrix[bot][right - i]

                # Move the stored top right value into the bottom right position
                matrix[bot][right - i] = top_right

                # Store the bottom left value
                bot_left = matrix[bot - i][left]

                # Move the stored bottom right value into the bottom left position
                matrix[bot - i][left] = bot_right

                # Move the stored bottom left value into the top left position
                matrix[top][left + i] = bot_left
            
            # Move the borders inward
            left += 1
            right -= 1