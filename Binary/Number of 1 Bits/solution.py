'''
Solution 1
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n >> 1

        return count
    
'''
Solution 2 (Slightly more optimized, still constant time)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n-1)

        return count