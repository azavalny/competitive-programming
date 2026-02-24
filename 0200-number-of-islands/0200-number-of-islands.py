class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        bfs/dfs question
        all edges of grid are water

        island formed when connected up, down, left, right but NOT diagonally like in example 2

        if cell is 1 do BFS on adjacent neighbors until you run out of 1's and increment sol
        for each cell you visit mark it as 0 so that you don't revisit
        """
        m, n = len(grid), len(grid[0])
        sol = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    #BFS
                    queue = deque([(r, c)])
                    print(queue)
                    while queue:
                        curX, curY = queue.popleft()
                        print(curX, curY)
                        if grid[curX][curY] == "1":
                            # mark visited
                            grid[curX][curY] = "0"
                            # visit neighboring land
                            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                # check boundaries
                                dx = direction[0]
                                dy = direction[1]
                                if 0 <= curX + dx < m and 0 <= curY + dy < n:
                                    if grid[curX + dx][curY + dy] == "1":
                                        queue.append((curX + dx, curY + dy))
                    sol+=1
        return sol