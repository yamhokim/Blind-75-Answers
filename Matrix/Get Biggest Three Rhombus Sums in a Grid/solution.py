import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ROWS = len(grid)
        COLS = len(grid[0])
        minheap = []

        for r in range(ROWS):
            for c in range(COLS):
                top, bottom = r, r
                left, right = c, c

                while bottom < ROWS and left >= 0 and right < COLS:
                    res = 0
                    if top == bottom:
                        res = grid[top][left]
                    else:
                        left_col, right_col = (left + right) // 2, (left + right) // 2
                        expand = True

                        for row in range(top, bottom + 1):
                            if left_col == right_col:
                                res += grid[row][left_col]
                            else:
                                res += grid[row][left_col] + grid[row][right_col]

                            if left_col == left:
                                expand = False

                            if expand:
                                left_col -= 1
                                right_col += 1
                            else:
                                left_col += 1
                                right_col -= 1
            
                    if len(minheap) < 3:
                        if res not in minheap:
                            heapq.heappush(minheap, res)
                    else:
                        if res > minheap[0] and res not in minheap:
                            heapq.heappop(minheap)
                            heapq.heappush(minheap, res)
                    bottom += 2
                    left -= 1
                    right += 1
                
        
        minheap.sort(reverse=True)

        return minheap