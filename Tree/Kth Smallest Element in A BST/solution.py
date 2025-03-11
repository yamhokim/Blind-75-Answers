'''
Iterative Solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root is None:
            return []
        
        res = []
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder(root)

        return res[k-1]
    

'''
Recursive Solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, arr):
        if root is None:
            return
        
        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)

        return arr

    def inorder(self, root):
        if root is None:
            return []
        
        return self.dfs(root, [])

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder(root)

        return res[k-1]