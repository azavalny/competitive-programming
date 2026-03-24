class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        subarray sums equals k but non overlapping arrays

        [1,1,1,1,1] target = 2

        {0: 1
        1: 1
        2: 1
        3: 1
        4: 1
        5: 1} curSum-2?

        [-1,3,5,1,4,2,-9] target = 6
        {
            0: 1
            -1: 1
            2: 1
            7: 1
            8: 1
            12: 1
            14: 1
            5: 1
        } curSum - 6?

        reset curSum if you've seen an answer and only increment sol by 1 to get non-overlapping subarrays
        """
        table = defaultdict(int, {0: 1})
        curSum = 0
        sol = 0

        for n in nums:
            curSum +=n
            if curSum-target in table:
                sol += 1
                curSum = 0
                table = defaultdict(int, {0: 1})
            table[curSum] +=1
        return sol