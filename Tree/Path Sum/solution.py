# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, root.val)]
        while len(stack) > 0:
            curr = stack.pop()
            if not curr[0].left and not curr[0].right and curr[1] == targetSum:
                return True
            
            if curr[0].left:
                stack.append((curr[0].left, curr[1] + curr[0].left.val))
            if curr[0].right:
                stack.append((curr[0].right, curr[1] + curr[0].right.val))
        
        return False