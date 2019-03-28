# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque()
        q.append((root, 1))
        depth = 1
        result = []
        tmp = []
        while len(q) > 0:
            node = q.popleft()
            if depth == node[1]:
                tmp.append(node[0].val)
            else:
                result.append(tmp)
                tmp = [node[0].val]
                
            depth = node[1]
            if node[0].left:
                q.append((node[0].left, node[1] + 1))
            if node[0].right:
                q.append((node[0].right, node[1] + 1))
        if len(tmp) > 0:
            result.append(tmp)
        result.reverse()
        return result