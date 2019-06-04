class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.values.append(x)
        if self.min is None or self.min > x:
            self.min = x
        

    def pop(self):
        """
        :rtype: None
        """
        self.values.pop()
        self.min = None
        for v in self.values:
            if self.min is None or self.min > v:
                self.min = v
        

    def top(self):
        """
        :rtype: int
        """
        return self.values[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()