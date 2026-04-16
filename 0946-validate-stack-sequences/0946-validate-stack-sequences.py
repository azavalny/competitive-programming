class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        push order fixed, check if popped is valid pop order to get empty stack

pushed =[1,2,3,4,5], popped = [4,5,3,2,1]
                                       i
stack:  [3 2 1]        

pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
                                      i
stack: [2 1] <-- 1 cannot be popped before 2


        loop over every n in pushed:
            if n equals ith value in popped:
                keep popping from pushed the ith value from popped until pushed[i] != popped[i]
            else:
                push next n
        if stack remmains return false else true
        """
        stack = deque()
        i = 0
        for n in pushed:
            stack.appendleft(n)
            curN = n
            while stack and curN == popped[i]:
                stack.popleft()
                i+=1
                if stack:
                    curN = stack[0]
        if stack:
            return False
        return True