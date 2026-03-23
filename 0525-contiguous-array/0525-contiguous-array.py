class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        0's == 1's
        0's - 1's == 0

        {diffs: first index}

num:     0 1  1  1  1  1  0  0  0
index:   0 1  2  3  4  5  6  7  8
diff:    1 0 -1 -2 -3 -4 -3 -2 -1
{1: 0
0: 1
-1: 2
-2: 3
-3: 4}
        if diffs match compare curIndex - first index
        """
        table = defaultdict(int, {0: -1})
        diff = 0
        sol = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                diff-=1
            else:
                diff+=1
            if diff not in table:
                table[diff] = i
            sol = max(sol, i-table[diff])
        return sol