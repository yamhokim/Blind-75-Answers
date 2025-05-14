class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        y_counts = [0, 0, 0]
        other_counts = [0, 0, 0]

        for r in range(ROWS):
            for c in range(COLS):
                # left diagonal of Y
                if r < ROWS // 2 and r == c:
                    y_counts[grid[r][c]] += 1
                # right diagonal of Y
                elif r < ROWS // 2 and r + c == ROWS - 1:
                    y_counts[grid[r][c]] += 1
                # middle stem of Y
                elif r >= ROWS // 2 and c == ROWS // 2:
                    y_counts[grid[r][c]] += 1
                # outside of Y
                else:
                    other_counts[grid[r][c]] += 1
        
        y_squares = sum(y_counts)
        other_squares = sum(other_counts)
        res = float('inf')

        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                res = min(res, y_squares - y_counts[i] + other_squares - other_counts[j])
    
        return res