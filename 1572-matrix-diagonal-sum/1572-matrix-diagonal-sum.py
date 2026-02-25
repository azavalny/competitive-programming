class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        (r, r) + (r, n-r-1)

        subtract middle at end

        [1,1,1,1]
        [1,1,1,1]
        [1,1,1,1]
        [1,1,1,1]
        """
        ROWS, COLS = len(mat), len(mat[0])
        curSum  = 0
        for r in range(ROWS):
            curSum += mat[r][r] + mat[r][ROWS-r-1]
        if ROWS%2 != 0:
            curSum -= mat[ROWS//2][COLS//2]
        return curSum