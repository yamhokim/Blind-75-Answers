'''
Recursive DFS Solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

'''
Iterative BFS Solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [root]
        depth = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            depth += 1

        return depth

'''
Iterative DFS Solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]
        max_depth = 1
        while len(stack) > 0:
            curr_node = stack.pop()
            max_depth = max(max_depth, curr_node[1])
            if curr_node[0].right:
                stack.append([curr_node[0].right, curr_node[1] + 1])
            if curr_node[0].left:
                stack.append([curr_node[0].left, curr_node[1] + 1])
            
        return max_depth
            