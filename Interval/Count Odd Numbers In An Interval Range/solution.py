class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        if length % 2:
            return length // 2 + (low % 2)
        else:
            return length // 2