class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        return length of array
        turbulent = pair of 2 numbers where one is greater than the other

        [9, 4, 2, 10, 7, 8, 8, 1, 9]
            ______________  _______
        _____
                  _________
            _____
                  _____
                      _____
                                ____
                            ____

        [4, 8, 12, 16] < - monotonically increasing/decreasing array has max turbulent len 2
        _____
            _____
                ______

            [9, 4, 2, 10, 7, 8, 8, 1, 9]
                   r
prevGreater: +
curLen: 2
maxLen: 2

        keep shifting right:
            if (nums[right] > nums[right-1] and prevGreater) or (nums[right] < nums[right-1] and prevGreater):
                reset curLen to 0

            if nums[right] > nums[right-1] and (prevGreater == False or prevGreater == None):
                flip prevGreater to true
            increment curLen
            update maxLen


        [9, 4, 2, 10, 7, 8, 8, 1, 9]
        """
        if len(arr) == 1:
            return 1
        prevGreater = False
        if arr[1] < arr[0]:
            prevGreater = True
        if len(arr) ==2 and arr[1] == arr[0]:
            return 1

        curLen = 1
        maxLen = 1
        for r in range(1, len(arr)):
            if (arr[r] >= arr[r-1] and not prevGreater) or (arr[r] <= arr[r-1] and prevGreater):
                curLen = 1
            
            if arr[r] < arr[r-1] and prevGreater == False:
                prevGreater = True
            if arr[r] > arr[r-1] and prevGreater == True:
                prevGreater = False

            if arr[r] == arr[r-1]:
                curLen-=1

            curLen +=1
            maxLen = max(maxLen, curLen)

        return maxLen