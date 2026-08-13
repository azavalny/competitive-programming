class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        circular array = ends end connects to beginning
            next of nums[i+1] = nums[(i + 1) % n]
                    nums[i-1] = nums[(i - 1 + n) % n]
        subarray has each element at most once

        total sum - min sum subarray = max sum subarray of circular
        """

        maxRes, minRes, maxSum, minSum = nums[0], nums[0],nums[0], nums[0]

        for right in range(1, len(nums)):
            maxSum = max(nums[right] + maxSum, nums[right])
            maxRes = max(maxSum, maxRes)

            minSum = min(nums[right] + minSum, nums[right])
            minRes = min(minSum, minRes)
            
        if maxRes < 0:
            return maxRes
        
        return max(maxRes, sum(nums)-minRes)
            