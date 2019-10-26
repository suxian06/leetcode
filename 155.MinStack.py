class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
    def push(self, x: int) -> None:
        self.min = self.getMin()

        if self.min == None or self.min > x:
            self.min = x
        self.stack.append((x,self.min))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]
