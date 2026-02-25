class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        rectangular or square

        m x n

           C
     R  [1,2,3]
        [4,5,6]

0, 1 => 1, 0

        n x m
        [1, 4]
        [2, 5]
        [3, 6]
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        sol = [[0 for r in range(ROWS)] for c in range(COLS)] # swap ROWS and COLUMNS

        for r in range(ROWS):
            for c in range(COLS):
                sol[c][r] = matrix[r][c]
        return sol