class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        every minute, fresh orange 4 directionally adjacent to rotten becomes rotten
            0-empty
            1-fresh
            2-rotten

        goal: min mins until no fresh oranges, otherwise -1 if impossible, 0 if no fresh oranges

        [2,2,2]
        [2,2,0]
        [0,2,2]
min:4 and fresh oranges remaining is 0
        BFS on all rotten oranges and for each time we add up to 4 neighbors in the queue we increment mins

        queue = [(0, 0), ...] starts with all rotten oranges
        fresh oranges count

        while queue and fresh > 0:
            get next cell
            if it's 1:
                 mark it 2
                 fresh oranges count decrements
            get cell's valid neighbors 4 directionally if they're fresh:
                add to queue
            increment minutes
        fresh count == 0?

        [2,2,2]
        [0,2,2]
        [1,0,2]
mins:4 but no solution bc 1
        """
        fresh = sum(cell == 1 for row in grid for cell in row)
        queue = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        mins=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:

            # process entire queue at once
            for cell in range(len(queue)):    
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    newR = r + dr
                    newC = c + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        fresh-=1
                        queue.append((newR, newC)) 
            mins+=1
        if fresh > 0:
            return -1
        return mins