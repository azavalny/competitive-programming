class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        [-4, 3, -2, 5, -8, 6, 2, -1, 4]
                           l
                                      r
curSum: -4   3   1  6  -2  6  8   7  11
maxSum: -4   3   3  6   6  6  8   8  11

    while r < len(nums):
        while curSum negative and left < right:
            shrink window and update current sum
        update current sum and increment right
        """
        curSum, maxSum, l, r = 0, float("-inf"), 0, 0
        while r < len(nums):
            if curSum < 0:
                curSum = 0
            curSum += nums[r]
            maxSum = max(maxSum, curSum)
            r+=1

        return maxSum