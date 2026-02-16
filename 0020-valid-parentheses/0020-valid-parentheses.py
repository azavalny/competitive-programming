class Solution:
    def isValid(self, s: str) -> bool:
        """
        open brackets must be closed by same type of bracket in correct order and every open bracket has corresponding closed bracket

        idea 1: use stack to store only open
            append open brackets
            if closing bracket and top of stack is the opened version then pop()
            otherwise s is invalid

            if stack at the end is not empty valid


    edge case: {{{
        always add when opening bracket

        stack = [{, {, {]

    edge case: }}}
        need to add closing brackets when top is not opening bracket
        stack = [}, }, }]

    edge case: {}
        add opening
        pop stack because closing matches opening
        
        stack = [{]
        
        """
        stack = []
        bracketMap = {")": "(", "}": "{", "]":"["} #closing: opening

        for b in s:
            if stack and b in bracketMap.keys() and bracketMap[b] == stack[-1]: # when b closing
                stack.pop()
            else:
                stack.append(b)
        if stack:
            return False
        return True