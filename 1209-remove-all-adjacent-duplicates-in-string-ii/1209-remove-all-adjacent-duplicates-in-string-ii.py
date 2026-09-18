class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        choose k adjacent equal chars and removing them

        why stack and not greedy if repeated operations?

        deeedbbcccbdaa, k=3
        deee
        ddbb
        ddbbccc
        ddbbb
        ddd
        aa


        pbbcggttciiippooaais, k=2

        pbb
        pc
        pcgg
        pc
        pctt
        pcc
        pii
        pipp
        pioo
        piaa
        pii
        ps

        keep adding to stack until next element becomes kth from top
        then pop them all and continue

        dixxxiit, k=3
        
        di
        dixxx
        diii
        dt

        seeee, k=4


        condense values in stack down to tuples of frequencies (d, 1), (e, 3) to avoid doing 10^4 extra operations
        """
        stack = deque([])
        for c in s:
            if len(stack) > 0 and stack[0][0] == c:
                top = stack.popleft()
                stack.appendleft((top[0], top[1]+1))

                if stack[0][1] == k:
                    stack.popleft()
            else:
                stack.appendleft((c, 1))
        sol = ""
        for c, freq in reversed(stack):
            sol += c*freq
        return sol

        
            