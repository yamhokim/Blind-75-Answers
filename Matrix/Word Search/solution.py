class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(row, col, idx):
            # Case where we've found all letters in correct order
            if idx == len(word):
                return True
            # Case where we're out of bounds
            elif row >= ROWS or col >= COLS or row < 0 or col < 0:
                return False
            # Case where the current square doesn't match the letter we need
            elif board[row][col] != word[idx]:
                return False
            # Case where we've already visited the square
            elif (row, col) in visited:
                return False

            visited.add((row, col))
            res = dfs(row + 1, col, idx + 1) or dfs(row, col + 1, idx + 1) or dfs(row - 1, col, idx + 1) or dfs(row, col - 1, idx + 1)
            visited.remove((row, col))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False