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
        """
        absMatrix = [[abs(c) for c in r] for r in matrix]
        absSum = sum([sum(row) for row in absMatrix])
        numNegatives = 0
        for r in matrix:
            for c in r:
                if c < 0:
                    numNegatives+=1
        leastAbsVal = float("inf")
        for r in matrix:
            for c in r:
                leastAbsVal = min(leastAbsVal, abs(c))
        if numNegatives%2 != 0:
            absSum -= 2*leastAbsVal
        return absSum