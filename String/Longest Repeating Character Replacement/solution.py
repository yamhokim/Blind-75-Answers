'''
O(26*n) Approach
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        running_max = 0
        counts = {}

        for end in range(len(s)):
            counts[s[end]] = 1 + counts.get(s[end], 0)
            while (end - start + 1) - max(counts.values()) > k:
                counts[s[start]] -= 1
                start += 1
            
            running_max = max(running_max, end - start + 1)

        return running_max

'''
O(n) Approach
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        running_max = 0
        counts = {}
        max_frequency = 0

        for end in range(len(s)):
            counts[s[end]] = 1 + counts.get(s[end], 0)
            max_frequency = max(max_frequency, counts[s[end]])
            while (end - start + 1) - max_frequency > k:
                counts[s[start]] -= 1
                start += 1

            running_max = max(running_max, end - start + 1)
        
        return running_max