class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = {}
        t_letters = {}

        for i in range(len(s)):
            if s[i] not in s_letters:
                s_letters[s[i]] = 1
            else:
                s_letters[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in t_letters:
                t_letters[t[i]] = 1
            else:
                t_letters[t[i]] += 1

        return s_letters == t_letters