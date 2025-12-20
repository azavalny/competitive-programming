class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sol = 0
        currentmax = 0
        for n in nums:
            if n == 1:
                currentmax +=1
                sol = max(currentmax, sol)
            if n == 0:
                currentmax = 0
        return sol