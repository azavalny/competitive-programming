class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1
        curLen = 1
        prev = 0
        for i in range(1, len(arr)):
            sign = (arr[i] > arr[i-1]) - (arr[i] < arr[i-1]) # +1, -1, or 0
            if sign == 0:
                curLen = 1
            elif sign == -prev:
                curLen +=1 #direction flipped, extend window
            else:
                curLen = 2 # same direction, new run of 2
            prev = sign
            maxLen = max(maxLen, curLen)
        return maxLen