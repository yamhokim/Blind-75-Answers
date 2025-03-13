class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        res = 0

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            if counts[s[i]] % 2 == 0:
                res += 2

        for count in counts.values():
            if count % 2 != 0:
                res += 1
                break

        return res