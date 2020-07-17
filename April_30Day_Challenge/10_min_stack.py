#!/usr/bin/python3

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:

        curr_min = self.getMin()

        if curr_min is None or x < curr_min:
            curr_min = x

        self.stack.append((x,curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



'''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__a = []

    def push(self, x: int) -> None:
        m = x
        if self.__a:
            m = self.__a[-1][1]
            if m > x:
                m = x
        self.__a.append((x, m))

    def pop(self) -> None:
        self.__a.pop()

    def top(self) -> int:
        return self.__a[-1][0]

    def getMin(self) -> int:
        return self.__a[-1][1]
'''
