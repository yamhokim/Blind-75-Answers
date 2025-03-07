'''
Initial Approach
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelSymmetric(self, level):
        start = 0
        end = len(level) - 1
        while start < end:
            if level[start] != level[end]:
                return False
            start += 1
            end -= 1
        
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = [root]
        level = []
        curr = root
        while len(queue) > 0:
            length = len(queue)
            for i in range(length):
                curr_node = queue.pop(0)
                if curr_node is None:
                    level.append(None)
                else:
                    if curr_node.left:
                        queue.append(curr_node.left)
                    else:
                        queue.append(None)
                    if curr_node.right:
                        queue.append(curr_node.right)
                    else:
                        queue.append(None)
                    level.append(curr_node.val)
            symmetric = self.levelSymmetric(level)
            if not symmetric:
                return False
            level = []
        
        return True
    
'''
Better Approach (NeetCode Implementation)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)