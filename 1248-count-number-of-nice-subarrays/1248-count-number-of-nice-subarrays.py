class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        # of subarrays with k odd numbers

        curOddCount -k in hashmap?
        hashmap = {prevOddCount: counts} intialized to {0: 1}
        """
        table = defaultdict(int, {0: 1})
        curOddCount = 0
        sol = 0
        for n in nums:
            if n%2 != 0:
                curOddCount +=1
            sol += table[curOddCount - k]
            table[curOddCount] +=1
        return sol