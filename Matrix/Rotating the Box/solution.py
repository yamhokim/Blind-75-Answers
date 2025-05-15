class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        res = []

        # Start by rotating 90 degrees clockwise
        for c in range(len(boxGrid[0])):
            row = []
            for r in range(len(boxGrid) - 1, -1, -1):
                row.append(boxGrid[r][c])
            res.append(row)
        
        # Perform gravity
        for c in range(len(res[0])):
            swap_idx = len(res) - 1
            for r in range(len(res) - 1, -1, -1):
                if res[r][c] == '#':
                    res[r][c], res[swap_idx][c] = res[swap_idx][c], res[r][c]
                    swap_idx -= 1
                elif res[r][c] == '*':
                    swap_idx = r - 1
        
        return res