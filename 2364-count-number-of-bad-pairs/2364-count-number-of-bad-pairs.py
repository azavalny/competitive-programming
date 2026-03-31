class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        bad pair = 2 nums where difference between 2nd and 1st's indexes != differences between values

        total number = {state: frequency}

# bad pair  nums[i]-i != nums[j] -j
# good pair nums[i]-i == nums[j] -j
{nums[i]-i : counts}


bad = total previous - good
bad = i - table[nums[i]-i]


    [4, 1, 3, 3]
i    0  1  2  3
n-i  4  0  1  0
bad  0  1  3  5

table={
    4: 1
    0: 2
    1: 1
}

        """
        table = defaultdict(int)
        sol = 0
        for i, n in enumerate(nums):
            sol += (i - table[n-i])
            table[n-i] +=1
        return sol