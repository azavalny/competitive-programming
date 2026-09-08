class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        square matrix
        
        can multiply adjacent elements by -1
        find max sum of matrix

        find absolute value sum
        find # of negative values
        if odd, assign least absolute value negative
        flip everything else positive

        abs_sum = 0
        neg_count = 0
        min_abs_value = float('inf')
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):
            for col in range(COLS):
                abs_sum += abs(matrix[row][col])
                if matrix[row][col] < 0:
                    neg_count += 1
                min_abs_value = min(min_abs_value, abs(matrix[row][col]))
        if neg_count % 2 != 0: #odd
            abs_sum -= 2*min_abs_value
        return abs_sum
        """
        numNegatives = 0
        leastAbsVal = float("inf")
        ROWS, COLS = len(matrix), len(matrix[0])
        absSum=0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] < 0:
                    numNegatives+=1
                leastAbsVal = min(leastAbsVal, abs(matrix[r][c]))
                absSum += abs(matrix[r][c])
        if numNegatives%2 != 0:
            absSum -= 2*leastAbsVal
        return absSum