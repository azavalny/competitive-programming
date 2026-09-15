class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        1 - server, 0 no server

        pair of servers communicate if on same row or same column (updownlefrtright)


        [1,1]
        [1,0]
col:
    0: 2
    1: 1
row: 
    0: 2
    1: 1

(0, 0)  (0, 1)  (1, 0)
+1          +1   +1  = 3


        [1,1,0,0]
        [0,0,1,0]
        [0,0,1,0] 
        [0,0,0,1]
for each server:
    if row count or col count> 1:
        add + 1

r:   c:
    {
    0:1
    1:1
    2:2
    3:1
    }
{
0:2
1:1
2:1
3:1
}




        maintain sets to count number of servers for each column and sets for each row


        """ 
        rowFreqs = {}
        colFreqs = {}
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowFreqs[r] = rowFreqs.get(r, 0) +1
                    colFreqs[c] = colFreqs.get(c, 0) +1
        sol = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if rowFreqs[r] > 1 or colFreqs[c] > 1:
                        sol +=1
        return sol