class Solution:
    def decodeString(self, s: str) -> str:
        """

        54[ab6[cd]]
stack: 5, 4, [, a, b, 6, ], c, d, ] 
        loop over each character:
            add character if not opening bracket
            if character is closing bracket:
                pop characters until opening bracket reached (including opening bracket)
            if character is number:
                add current string to stack number times
        """
        stack = deque()

        for i, c in enumerate(s):
            if c != "]":
                stack.appendleft(c)
            else: # closing bracket
                substring = ""
                while stack[0] != "[":
                    substring = stack.popleft() + substring # add to beginning because stack reverses
                stack.popleft() # remove "["
                k = ""
                while stack and stack[0].isdigit(): #get digit
                    k = stack.popleft() + k
                stack.appendleft(substring*int(k))
        return "".join(reversed(stack))
