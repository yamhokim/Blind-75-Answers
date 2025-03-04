'''
Recursive Approach (Post-Order Traversal)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        temp_right = root.right
        root.right = root.left
        root.left = temp_right

        return root
    

'''
Iterative Approach (BFS)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = [root]

        while len(queue) > 0:
            curr_node = queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            
            
            temp_right = curr_node.right
            curr_node.right = curr_node.left
            curr_node.left = temp_right

        return root