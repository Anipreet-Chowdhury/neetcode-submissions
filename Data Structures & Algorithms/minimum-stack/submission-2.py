class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = None
        self.prev = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val == self.minval:
            self.prev.append(val)
        elif self.minval is None:
            self.minval = val
        elif val < self.minval:
            self.prev.append(self.minval)
            self.minval = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minval:
            if len(self.prev) > 0:
                self.minval = self.prev.pop()
            else:
                self.minval = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval
