class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = ""
        c = 0
        while n != 0:
            m = (n - 1) % 26
            out = chr(ord('A') + m) + out
            n = (n - 1) // 26
        return out