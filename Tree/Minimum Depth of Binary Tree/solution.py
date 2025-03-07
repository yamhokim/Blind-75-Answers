# Initially I thought of using the same approach as maximum depth of binary tree, but then this would not work for edge cases where every node has 1 child, essentially creating a linked list.
# The tree would take the minimum depth as the depth of the root of the tree, but that'd be incorrect since its not a leaf node.
# Need to figure out a way to modify the original algorithm to only look for leaf nodes.
# I still think that DFS is the proper way to go.
# Potentially add a check to see if the current node has no children, only if it passes this check will we actually take the node's depth into consideration

# After doing some research, it seems that BFS or level order traversal is a better method
# We go level by level and return the depth of the first leaf node encountered, that is the minimum depth
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [root]
        depth = 0
        while len(queue) > 0:
            length = len(queue)
            depth += 1
            for i in range(length):
                curr = queue.pop(0)
                if curr.left and curr.right:
                    queue.append(curr.left)
                    queue.append(curr.right)
                elif curr.left:
                    queue.append(curr.left)
                elif curr.right:
                    queue.append(curr.right)
                else:
                    return depth