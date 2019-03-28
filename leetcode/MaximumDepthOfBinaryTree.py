# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth1(root.left), self.maxDepth1(root.right))
        
    def maxDepth2(self, root: TreeNode) -> int:
        if root == None:
            return 0
        q = deque()
        q.append((root, 1))
        depth = 1
        while len(q) > 0:
            node = q.popleft()
            if node[0].left != None:
                q.append((node[0].left, node[1] + 1))
            if node[0].right != None:
                q.append((node[0].right, node[1] + 1))
            depth = node[1]
        return depth