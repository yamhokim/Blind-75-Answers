class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0])
        bot = len(matrix)

        res = []

        while left < right and top < bot:
            # Move right along the top border
            for c in range(left, right):
                res.append(matrix[top][c])
            
            # Move the top border down by 1 row
            top += 1

            # Move down along the right border
            for r in range(top, bot):
                res.append(matrix[r][right - 1])
            
            # Move the right border left by 1 column
            right -= 1

            # Run an intermediate check of the condition
            if not (left < right and top < bot):
                break

            # Move left along the bot border
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bot - 1][c])

            # Move the bot border up by 1 row
            bot -= 1

            # Move up along the left border
            for r in range(bot - 1, top - 1, -1):
                res.append(matrix[r][left])
            
            # Move the left border right by one column
            left += 1
            
        return res