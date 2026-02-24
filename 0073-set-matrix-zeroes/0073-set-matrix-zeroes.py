class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        matrix cannot be empty but can be [[1]]

        [1, 1, 1], 
        [1, 0, 1], 
        [1, 1, 1]
        """
        first_row_has_zero = False
        first_col_has_zero = False

        rows, cols = len(matrix), len(matrix[0])

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True

        # if cell has 0 we set corresponding row and column of first row and first column to 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0


        # if first row or first column marked then set rest of row or column to 0's
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0