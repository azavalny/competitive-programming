class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        magic square = each row, col, both diagonals have same sum AND numbers distinct numbers from 1-9
        count 3x3 magic square subgrids

        slide 3x3 window left to right and top to bottom across grid and increment count
            O(n^2) if you use optimization of removing last and adding next, O(9*n^2 otherwise)

        for i in (0, m-3, 3):
            for j in range(0, n-3, 3):
                count += isMagicSquare(grid[i:i+3][j:j+3]) #O(9)

        [[4, 3, 8, 4],
         [9, 5, 1, 9],
         [2, 7, 6, 2]]

        [[4, 3, 8, 4],
         [9, 5, 1, 9],
         [2, 7, 6, 2],
         [2, 7, 6, 2],
         [2, 7, 6, 2]]
        """
        def isMagicSquare(subgrid):
            # check rows, columns, diagonals have same sum
            m, n = len(subgrid), len(subgrid[0])
            sums = set()
            for row in range(m):
                rowSum = 0
                for col in range(n):
                    rowSum += subgrid[row][col]
                sums.add(rowSum)

            for col in range(n):
                colSum = 0
                for row in range(m):
                    colSum += subgrid[row][col]
                sums.add(colSum)

            diagSum1 = 0
            for r in range(m):
                diagSum1 += subgrid[r][r]
            sums.add(diagSum1)
            diagSum2 = 0
            for r in range(m):
                diagSum2 += subgrid[r][n-r-1]
            sums.add(diagSum2)
            
            if len(sums) > 1:
                return False
            # check distinct values
            unique = set()
            for row in subgrid:
                for val in row:
                    if val < 1 or val > 9:
                        return False
                    unique.add(val)
            if len(unique) != 9:
                return False
            return True
        count=0
        m, n = len(grid), len(grid[0])
        for c in range(n-2):
            for r in range(m-2):
                count += isMagicSquare([row[c:c+3] for row in grid[r:r+3]])
        return count