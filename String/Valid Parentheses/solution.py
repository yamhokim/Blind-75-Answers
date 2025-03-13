class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {")": "(", "]": "[", "}": "{"}
        if s[0] in bracket_pairs:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in bracket_pairs:
                if stack and stack[-1] == bracket_pairs[s[i]]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])
        
        return True if len(stack) == 0 else False