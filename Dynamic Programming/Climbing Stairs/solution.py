'''
Memoization Approach
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(curr):
            if curr > n:
                return 0
            elif curr == n:
                return 1
            elif curr in memo:
                return memo[curr]
            
            memo[curr] = dfs(curr + 1) + dfs(curr + 2)
            return memo[curr]
        
        return dfs(0)
    

'''
Bottom Up DP Solution
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n-1):
            temp_one = one
            one = one + two
            two = temp_one

        return one