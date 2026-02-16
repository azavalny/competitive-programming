class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        idea 1: use stack to keep track of operations (parenthesis) and undo them

            e.g. [d1/, ../] undo each other like "(" and ")"

            don't push "./" to stack

        """
        stack = []
        for l in logs:
            if l != "./":
                if l == "../" and stack:
                    stack.pop()
                if l != "../":
                    stack.append(l)
        return len(stack)