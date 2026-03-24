class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        number of subarrays with sum equal to goal

        idea 1: hashing
        curSum - goal in hashmap?
        {prevSum: counts}

        idea 2: sliding window because window sum is always monotonically increasing
        increment right pointer if sum less than goal while holding left pointer steady
        increment left pointer while holding right pointer steady if sum greater than goal
        """
        table = defaultdict(int, {0: 1})
        curSum = 0
        sol = 0
        for n in nums:
            curSum +=n
            sol += table[curSum - goal]
            table[curSum] +=1
        return sol