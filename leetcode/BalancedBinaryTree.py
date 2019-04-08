# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if node is None:
                return 0
            ld = dfs(node.left)
            rd = dfs(node.right)
            return -1 if ld == -1 or rd == -1 or abs(ld - rd) > 1 else 1 + max(ld, rd)
        return dfs(root) != -1