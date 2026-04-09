class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        # of subarrays filled with 0

        [0, 0, 0, 2, 0, 0]
               i

    for n in nums:
        if isZeroWindow:
            keep acumulating curSum += i - window start + 1
        else:
            keep reseting the zero window start and curSum
            add to sol if curSum != 0

        
        [0] = 1
        [0, 0] = 2 + 1
        [0, 0, 0] = 3 + 3
        [0, 0, 0, 0] = 4 + 6
        [0, 0, 0, 0, 0] = 5 + 10
        = # 0's + prev

        """
        sol = 0
        curSum = 0
        windowStart = 0
        prevZero = False
        for i, n in enumerate(nums):
            if n == 0:
                if not prevZero:
                    windowStart = i
                curSum = i - windowStart + 1 + curSum
                prevZero = True
            else:
                if prevZero:
                    sol += curSum
                curSum = 0
                windowStart = i
                prevZero = False
        if curSum > 0:
            sol += curSum
        return sol
        
        