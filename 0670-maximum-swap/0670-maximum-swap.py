class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        swap 2 digits at a time to get max valued number
            return max valued number
        2736
        7236

        don't need to be adjacent

        goal: bubble largest value to the left
        
        80091
        90081

        find max after current index (>=) and see if we can swap and return otherwise keep iterating

maxRightmostMax
        (val, index)
        (8, 1)   (2, 4) (2,4)  (2, 4)  -inf
        8 8 0 2 2
            i
        """
        numArr = [int(i) for i in list(str(num))]
        rightMostMax = deque([])
        currMax = numArr[-1]
        currMaxIndex = len(numArr)-1
        for i in range(len(numArr)-1, -1, -1):
            if numArr[i] > currMax:
                currMax = numArr[i]
                currMaxIndex = i
            rightMostMax.appendleft((currMax, currMaxIndex))
        print(rightMostMax)
        for i in range(len(numArr)):
            currentVal = numArr[i]
            print(currentVal, i)
            if currentVal < rightMostMax[i][0]: # found swap
                numArr[i] = rightMostMax[i][0]
                numArr[rightMostMax[i][1]] = currentVal
                return int("".join([str(i) for i in numArr]))
        return num
                