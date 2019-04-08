# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        
        def toBST(l, u):
            if l > u:
                return None
            m = (l + u) // 2
            node = TreeNode(nums[m])
            if l != u:
                node.left = toBST(l, m - 1)
                node.right = toBST(m + 1, u)
            return node
        return toBST(0, len(nums) - 1)

    def sortedArrayToBST2(self, nums):
        if (not nums) or len(nums) == 0:
            return None
        m = (len(nums) - 1) // 2
        root = TreeNode(nums[m])
        queue = deque()
        queue.append((root, (0, m, len(nums) - 1)))
        while len(queue) > 0:
            node, index = queue.popleft()
            if index[1] > index[0]:
                m = (index[0] + index[1] - 1) // 2
                node.left = TreeNode(nums[m])
                queue.append((node.left, (index[0], m, index[1] - 1)))
            if index[1] < index[2]:
                m = (index[1] + 1 + index[2]) // 2
                node.right = TreeNode(nums[m])
                queue.append((node.right, (index[1] + 1, m, index[2])))
        return root
        
if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    sl = Solution()
    tree = sl.sortedArrayToBST(nums)
    print(tree)