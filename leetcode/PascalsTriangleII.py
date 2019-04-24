class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        fa = [1]
        result = [0]
        for i in range(1, rowIndex+1):
            fa.append(fa[-1]*i)
            result.append(0)
        for i in range((rowIndex)//2+1):
            result[i] = fa[rowIndex]//(fa[i]*fa[rowIndex-i])
            result[rowIndex-i] = result[i]
        return result