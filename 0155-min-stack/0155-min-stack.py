class MinStack:
    """
    stack operations in O(1)
    
    idea 1: 2nd must always be increasing so getMin() returns first element if it exists
        top O(1) is always greatest element
        reject because undoing violation in push() is O(n)
    
    approach:
            maintain a stack with (current, minimum so far)
            append to stack and update minimum so far if new minimum found
            pop from last and also removes minimum at that element
    
        [-2, 0, -3]
stack=  [(-2, -2), (0, -2)]
    """

    def __init__(self):
        self.stack = [] #(value, min so far)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()