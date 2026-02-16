class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        for each operation:
            number: add number
            sum of previous two scores
            double previous
            remove previous score

        idea 1: basic stack
            add each previous operation to list and on "C" you pop()

        can't use regular array because C followed by D would give incorrect answer
        Undoing an operation is the key
        """
        stack = []
        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(2*stack[-1])
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)