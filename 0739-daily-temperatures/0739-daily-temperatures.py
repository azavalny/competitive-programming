class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        each value is # days you have to wait for next greatest temp on right
            store difference between current and next greatest temp otherwise 0 if none
        
        use monotonic decreasing stack (index, value)

        last value always zero

        [1, 2, 4, 3]

stack: [(2, 4), (3, 3)]
sol:  [1, 1, 0, 0]

        [73, 74, 75, 71, 69, 72, 76, 73]
                                     i
stack: [(6, 76), (7, 73)]
sol: [1, 1, 4, 2, 1, 1, 0, 0]


        [3, 2, 1]
stack:
sol:    [0, 0, 0]
        """
        sol = [0]*len(temperatures)
        stack = [] # (index, value)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                sol[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t))
        return sol