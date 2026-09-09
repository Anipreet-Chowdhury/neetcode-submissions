class MinStack:

    def __init__(self):
        self.stack = []
        self.mine = None
        self.prev = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mine == None:
            self.mine = val
        elif self.mine == val:
            self.prev.append(val)
        else:
            temp = self.mine
            self.mine = min(self.mine,val)
            if self.mine != temp:
                self.prev.append(temp)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mine:
            if len(self.prev) > 0:
                self.mine = self.prev.pop()
            else:
                self.mine = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mine
