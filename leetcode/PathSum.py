class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        def check(root, cur):
            if not root.left and not root.right:
                if root.val + cur == sum:
                    return True
                else:
                    return False
            l = False
            r = False
            if root.left:
                l = check(root.left, root.val + cur)
            if root.right:
                r = check(root.right, root.val + cur)
            return l or r
        return check(root, 0)

    def hasPathSum2(self, root, sum):
        if not root:
            return False
        q = [(root, 0)]
        while len(q) > 0:
            node, cur = q.pop(-1)
            if not node.left and not node.right and node.val + cur == sum:
                return True
            if node.right:
                q.append((node.right, node.val + cur))
            if node.left:
                q.append((node.left, node.val + cur))
        return False