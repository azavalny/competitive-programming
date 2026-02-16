class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        evaluate expression
        use floor in division
        no division by zero in input

        because undoing operations when completed use stack

        idea 1: stack to store numbers
            when operation reached:
                evaluate operation on previous two values and push to stack
            if not operation append number
        
        approach:
            append only numbers
            if operations: pop last two and perform operations and append final result
            valid arthematic means stack would have one value at end

        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
stack:  [22]        
        """
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]