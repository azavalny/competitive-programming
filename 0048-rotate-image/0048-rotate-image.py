class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        transpose then reverse rows
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # transpose:
        for r in range(ROWS):
            for c in range(r+1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(ROWS):
            matrix[r].reverse()