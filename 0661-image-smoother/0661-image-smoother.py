class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        Find average of nine cells (rounded down) in new matrix

        dirs = [(0,0), (-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        make sure to count #ignores and subtract it from denominator or count the ones you're going to use

        apply filter on each cell

        [0,1,1]
        [1,0,1]
        [1,1,0]
        """
        ROWS, COLS = len(img), len(img[0])

        sol = [[0 for c in range(COLS)] for r in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                counts = 0
                curSum = 0
                for dr, dc in [(0,0), (-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    newRow = dr + r
                    newCol = dc + c
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS:
                        counts+=1
                        curSum += img[newRow][newCol]
                sol[r][c] = curSum//counts
        return sol