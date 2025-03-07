'''
Approach 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateHeight(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.calculateHeight(root.left), self.calculateHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_height = self.calculateHeight(root.left)
        right_height = self.calculateHeight(root.right)

        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    

'''
Approach 2 (NeetCode Approach)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root is None:
            return [0, True]
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        height = max(left[0], right[0])
        balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

        return [1 + height, balanced]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
        