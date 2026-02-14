class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        min length of subarray whose sum is greater than or equal to target
        nums are all positive

        [2, 3, 1, 2, 4,  3] target=7
         L
                  R
                  L->L
                         R   
winSum   2  5  6  2  6   9

        move forward L pointer once winSum exceeds target until it dosen't then continue with R pointer
        each time window is valid update sol
        """
        l = 0
        winSum = 0
        sol = float("inf")
        for r in range(len(nums)):
            winSum += nums[r]
            while winSum >= target:
                sol = min(sol, r - l + 1)
                winSum -= nums[l]
                l+=1

            if winSum >= target:
                sol = min(sol, r - l + 1)
        if sol == float("inf"):
            return 0
        return sol