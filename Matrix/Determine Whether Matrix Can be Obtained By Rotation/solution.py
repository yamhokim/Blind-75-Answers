class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            left = 0
            right = len(mat[0]) - 1

            while left < right:
                for i in range(right - left):
                    top, bot = left, right

                    top_right = mat[top + i][right]
                    mat[top + i][right] = mat[top][left + i]
                    bot_right = mat[bot][right - i]
                    mat[bot][right - i] = top_right
                    bot_left = mat[bot - i][left]
                    mat[bot - i][left] = bot_right
                    mat[top][left + i] = bot_left
                left += 1
                right -= 1

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
            
        return False