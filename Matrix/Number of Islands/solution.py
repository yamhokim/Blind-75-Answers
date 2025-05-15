class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] != '0':
                    dfs(r + dr, c + dc)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands