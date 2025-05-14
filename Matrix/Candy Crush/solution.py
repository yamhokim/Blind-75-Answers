class Solution:
    def candyCrush(self, board):
        # 1. Start by checking if the board is valid
        if not board:
            return board

        # Keep a boolean value which checks whether the board is in a stable state or not
        stable = True

        # 2. Go through the rows and mark candies to crush (looking for horizontal groups to crush)
        # Note that we'll be using a sliding window of size three, since that the minimum number of candies we need to be the same to crush
        for r in range(len(board)):
            for c in range(len(board[r]) - 2):
                # We're taking the absolute since there's a chance that the number is negative (meaning its already been marked to be crushed)
                num1 = abs(board[r][c])
                num2 = abs(board[r][c + 1])
                num3 = abs(board[r][c + 2])

                # Check that all three values are the same and that they're not zero, if so, mark to be crushed
                if num1 == num2 and num2 == num3 and num1 != 0:
                    # Mark the candies to be crushed by making thme negative
                    board[r][c] = -num1
                    board[r][c + 1] = -num2
                    board[r][c + 2] = -num3

                    # Board is no longer stable
                    stable = False

        # 3. Go through the columns and mark the candies to crush (looking for vertical groups to crush)
        # Same logic as for rows, but looking for vertical groups now
        for c in range(len(board[0])):
            for r in range(len(board) - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r + 1][c])
                num3 = abs(board[r + 2][c])

                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r + 1][c] = -num2
                    board[r + 2][c] = -num3
                    stable = False

        # 4. Move candies down (gravity step)
        # Since we're working with gravity, we only look at columns
        for c in range(len(board[0])):
            # We'll be moving up the column since we want all noncrushed candies to be at the bottom
            swapIndex = len(board) - 1
            for r in range(len(board) - 1, -1, -1):
                # Whenever we come across a spot that's a non-crushed candy and isn't empty
                if board[r][c] > 0:
                    board[swapIndex][c] = board[r][c]
                    swapIndex -= 1

            # Now that all the candies have been moved to the bottom, everything above should be turned into empty space
            for r in range(swapIndex, -1, -1):
                board[r][c] = 0

        # Return the board if it is currently stable, if not, repeat
        return board if stable else self.candyCrush(board)
