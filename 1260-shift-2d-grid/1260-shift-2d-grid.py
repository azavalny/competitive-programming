class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        brute force:
        shift grid k times:
            store grid[i][n-1], grid[m-1][n-1] in temp to prevent overwriting from grid[i][j]
            grid[i][j+1] = grid[i][j]
            grid[i+1][0] = grid[i][n-1]
            grid[0][0] = grid[m-1][n-1]

        convert to 1d then rotate array problem then convert it back
        1 2 3 4 5 6 7 8 9
        9 1 2 3 4 5 6 7 8
        index = r*n + c
        rotate 1dList
        new_index = (index + k)% (m*n)
        new_r, new_c = (index - c)// r
        res[new_r][new_c] = grid[r][c]

        [[1,2,3],[4,5,6],[7,8,9]]
    ==> [1,2,3,4,5,6,7,8,9]
        rotate ^

        for each row r
            for each col c
                index = r*n + c
                new_index = (index + k)%(m*n) in list
                target_r = (new_index+1)//n - 1
                target_c = (new_index+1)%m - 1
                sol[target_r][target_c] = grid[r][c]
        """
        ROWS, COLS = len(grid), len(grid[0])
        sol = [[0 for col in range(COLS)] for row in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                curIndex = r*COLS + c
                new_index = (curIndex + k)%(ROWS*COLS)
                target_r = (new_index)//COLS
                target_c = (new_index)%COLS
                sol[target_r][target_c] = grid[r][c]

        return sol