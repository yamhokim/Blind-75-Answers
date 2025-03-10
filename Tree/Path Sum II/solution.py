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
    def dfs(self, curr, path, running_sum, targetSum, res):
        if not curr.left and not curr.right and running_sum == targetSum:
            res.append(path)
            return
        if curr.left:
            self.dfs(curr.left, path + [curr.left.val], running_sum + curr.left.val, targetSum, res)
        if curr.right:
            self.dfs(curr.right, path + [curr.right.val], running_sum + curr.right.val, targetSum, res)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if root is None:
            return res

        self.dfs(root, [root.val], root.val, targetSum, res)

        return res
    
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        stack = [[root, root.val, [root.val]]]

        while len(stack) > 0:
            curr_node, curr_sum, curr_path = stack.pop()
            if not curr_node.left and not curr_node.right and curr_sum == targetSum:
                res.append(curr_path)
            
            if curr_node.left:
                stack.append([curr_node.left, curr_sum + curr_node.left.val, curr_path + [curr_node.left.val]])
            if curr_node.right:
                stack.append([curr_node.right, curr_sum + curr_node.right.val, curr_path + [curr_node.right.val]])

        return res