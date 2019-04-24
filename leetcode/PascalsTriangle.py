class Solution:
    def generate(self, numRows):
        if numRows < 1:
            return []
        result = [[1]]
        for i in range(2, numRows+1):
            p = result[-1]
            l = [1]
            for j in range(1, i-1):
                l.append(p[j] + p[j-1])
            l.append(1)
            result.append(l)
        return result