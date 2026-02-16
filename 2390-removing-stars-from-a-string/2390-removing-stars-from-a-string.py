class Solution:
    def removeStars(self, s: str) -> str:
        """
        remove closest (by index) non star character to its left and the star itself
        input lowercase letters and *

        a * b *
        i
        * * *
            i

        use stack to store value of letters
        a*b*
stack = []

        leet**cod*e
        i
stack = [l e c o e]

       * a b *
stack = []
        """
        stack = [] # storing letters
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)