class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        length of smallest subarray to remove to get sum of elements divisible by p

        Remove a subarray whose sum = total sum%p

        (total-removed)%p == 0
        total%p = removed%p
            total sum%p = 10%6 = 4        

        
         3, 1, 4, 2  p=6
curSum   3  4  8  10
curSum%p 3  4  2  4

curSum-x = remainder
x = curSum-remainder
        {curSum: lastIndex}
        """
        total = sum(nums)
        remainder = total%p
        if remainder == 0:
            return 0
        curSum=0
        sol = len(nums)
        table = defaultdict(int, {0: -1})

        for i, n in enumerate(nums):
            curSum = (curSum + n)%p
            prefix = (curSum-remainder)%p # x = curSum - remainder
            if prefix in table:
                sol = min(sol, i-table[prefix])
            table[curSum] = i
            
        if sol == len(nums):
            return -1
        return sol