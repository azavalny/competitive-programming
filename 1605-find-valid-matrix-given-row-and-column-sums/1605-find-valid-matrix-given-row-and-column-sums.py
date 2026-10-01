class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        """
        sum of ith row and jth columns

        find any matrix with 0 or positive integers with the row and column sums

         rowSum = [3,8]
         colSum = [4,7]
        
        initialize with 0s
        0 0
        3 0 = 0
        1 7 = 0      

        greedy solution: 
        for each cell
            if both rowsum[i] and colSum[j] are not 0:
                choose min(rowSum[i], colSum[j]) and set it to be value
                    subtract value you chose from both rowSum[i] and colSum[j]
                    
        neetcode:  try sum up all rows for first column and then any leftover values move to later columns for each col
        
        0 0 0
        5 0 0 = 0
        3 4 0 = 0
        0 2 8 = 0
        """
        ROWS, COLS = len(rowSum), len(colSum)
        sol = [[0 for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if rowSum[r] > 0 and colSum[c] > 0:
                    new_value = min(rowSum[r], colSum[c])
                    rowSum[r] -= new_value
                    colSum[c] -= new_value
                    sol[r][c] = new_value
        return sol