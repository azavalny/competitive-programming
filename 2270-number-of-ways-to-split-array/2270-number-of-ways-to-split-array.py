class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        valid split  = sum first i+1 elements >= sum last n-i-1 elements 
            at least 1 element right of i <-- we have to stop at len(nums)-2

        prevSum >= curSum

        [10, 4, -8, 7]
curSum   10  14  6  13
endSum   13   3  -1  7
        [2, 3, 1, 0]
curSum   2  5  6  6
endSum   6  4  1  0
        """
        total = sum(nums)
        curSum = 0
        sol = 0

        for i in range(len(nums)-1):
            curSum += nums[i]
            prevSum = total - curSum
            if curSum >= prevSum:
                sol +=1
        return sol