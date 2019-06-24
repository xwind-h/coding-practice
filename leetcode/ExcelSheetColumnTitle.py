class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = ""
        while n != 0:
            m = (n - 1) % 26
            out = chr(ord('A') + m) + out
            n = (n - 1) // 26
        return out