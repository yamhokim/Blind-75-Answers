class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        start = 0
        running_max = 0

        for end in range(len(s)):
            while s[end] in substring:
                substring.remove(s[start])
                start += 1
            
            substring.add(s[end])
            length = end - start + 1
            running_max = max(running_max, length)

        return running_max