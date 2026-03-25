class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        subarray of length at least two and sum of elements divisible by k

        curSum%k == prevSum%k
        where length at least 2 

        [23,2,4,6,7], k=6

        {prevSum%k : index first seen}
{
    0: -1
    5: 0
    1: 1
}

        """
        table = defaultdict(int, {0: -1})
        curSum = 0

        for i, n in enumerate(nums):
            curSum +=n
            if curSum%k in table and i-table[curSum%k] >= 2:
                return True
            if not curSum%k in table:
                table[curSum%k] = i
        return False
