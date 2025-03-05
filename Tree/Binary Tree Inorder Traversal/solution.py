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
    def inorder(self, root, arr):
        if root is None:
            return None
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

        return arr

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        return self.inorder(root, [])

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = []
        output = []
        curr = root

        while len(stack) > 0 or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right

        return output
