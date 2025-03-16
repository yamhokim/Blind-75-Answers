class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_chars = {}
        s_chars = {}
        for c in t:
            if c in t_chars:
                t_chars[c] += 1
            else:
                t_chars[c] = 1
                s_chars[c] = 0

        start = 0
        have = 0
        need = len(t_chars)
        res = [-1, -1]
        resLen = float('inf')

        for end in range(len(s)):
            curr_c = s[end]
            if curr_c in s_chars:
                s_chars[curr_c] += 1
                if s_chars[curr_c] == t_chars[curr_c]:
                    have += 1

            while have == need:
                if (end - start + 1) < resLen:
                    res = [start, end]
                    resLen = end - start + 1
                
                if s[start] in s_chars:
                    s_chars[s[start]] -= 1
                    if s_chars[s[start]] < t_chars[s[start]]:
                        have -= 1

                start += 1

        start, end = res
        return s[start:end + 1] if resLen != float('inf') else ""