class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1, 1, 1, 1, 1, 1] k=3
        # [1, 2, 3, 4, 5, 6]]
        sol=0
        curSum = 0
        prefixSums = {0:1 }
        for n in nums:
            curSum +=n
            if curSum-k in prefixSums:
                sol += prefixSums.get(curSum-k)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return sol