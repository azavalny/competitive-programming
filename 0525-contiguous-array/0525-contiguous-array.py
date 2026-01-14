class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        max length of subarray with # 0's = # 1's

        [ 1 1 1 0 0]
#1s: 3
#0s: 2
diff: index
{
    1:0
    2: 1
    3: 2
}
3-2=1 : 0 -4 = 3 solution


            [0, 1, 0]
1s: 1
0s: 2
{
    0:1
    1: 0
}

2-1 = 1 : 0 - 2 = 2

            [0, 1, 1, 1, 1, 1, 0, 0, 0]
                                     i
numZeros    1   1

        """

        zeros=0
        ones=0
        diffs={} # count[1] - count[0]: ending index
        sol=0

        for i, n in enumerate(nums):
            if n == 0:
                zeros+=1
            if n == 1:
                ones+=1
                
            if ones - zeros not in diffs:
                diffs[ones - zeros] = i
            # best case if end
            if ones == zeros:
                sol = ones + zeros
            else:
                sol = max(sol, i - diffs[ones - zeros])
        return sol