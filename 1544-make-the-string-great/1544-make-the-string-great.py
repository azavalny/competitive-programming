class Solution:
    def makeGood(self, s: str) -> str:
        """
        good string:
        for each character:
            no two adjacent characters where 2nd is upper case version (greater than the first)
        
        empty string is good
        aB
        Ba

        wrong:
        idea 1: sliding window of size 2:
            check if 2nd character is uppercase version of first (32 + lowercase)
            remove both from s and check again

        idea 2: decreasing stack <-- not needed

        idea 2: stack
        abBAcC
            i
        
        stack = []

        append to stack if stack is empty
        check if property is violated before adding current element
        if violated:  lower(previous) = lower(current) and [current.islower() == previous.isupper()
                        or current.isupper() == previous.islower()]
            pop and ignore current
        else:
            append(current)
        runtime: O(n)

        "ab"
        stack = [a]
        current = b
        previous = a
        violated = true == true and a == b
        """
        stack = []
        for c in s:
            if stack and stack[-1].lower() == c.lower() and (c.islower() == stack[-1].isupper() or c.isupper() == stack[-1].islower()):
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)