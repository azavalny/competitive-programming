class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        1. (optimal) = update max if average (rounded up) is greater than current max
        2. binary search on range from min(nums) to max(nums) and iterate on prefix sum 
        """
        sol = nums[0]
        total = sol

        for i in range(1, len(nums)):
            total += nums[i]
            sol = max(sol, math.ceil(total / (i + 1)))
        return sol