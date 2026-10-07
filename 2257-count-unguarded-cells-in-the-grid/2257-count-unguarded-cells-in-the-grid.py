class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        """
        guard sees every cell in 4 directions until they reach wall/another guard
        cell is guarded if at least one guard sees it

        return # of empty unguarded cells

        explore each guard + mark each cell you visit
            return m*n - marked - # guards - # of walls to get complement
            m*n * #guards = n^3
CURRENT GUARD 1 5
UP: 0 5
GOING RIGHT 1 6
GOING LEFT 1 4
GOING LEFT 1 3
GOING LEFT 1 2
GOING LEFT 1 1
GOING LEFT 1 0
CURRENT GUARD 1 1
UP: 0 1
GOING RIGHT 1 2
GOING RIGHT 1 3
GOING RIGHT 1 4
GOING RIGHT 1 5
GOING RIGHT 1 6
GOING LEFT 1 0
CURRENT GUARD 1 6
UP: 0 6
GOING LEFT 1 5
GOING LEFT 1 4
GOING LEFT 1 3
GOING LEFT 1 2
GOING LEFT 1 1
GOING LEFT 1 0
CURRENT GUARD 0 2
GOING DOWN 1 2
GOING RIGHT 0 3
GOING LEFT 0 1
GOING LEFT 0 0
[1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1]

[0, 0, g, w, 0, w, w]
[0, g, 0, 0, 0, g, g]
WALLS {(0, 6): 1, (0, 3): 1, (0, 5): 1}
GUARDS {(1, 5): 1, (1, 1): 1, (1, 6): 1, (0, 2): 1}
        """
        ROWS, COLS = m, n
        marked = [[0 for i in range(COLS)] for _ in range(ROWS)]

        walls_locations = {tuple(coordinate): 1 for coordinate in walls}
        guards_locations = {tuple(coordinate): 1 for coordinate in guards}


        
        for guard_x,guard_y in guards:
            # up
            for r in range(guard_x-1, -1, -1):
                if (r, guard_y) in walls_locations or (r, guard_y) in guards_locations:
                    break
                marked[r][guard_y] = 1
            # down
            for r in range(guard_x+1, ROWS):
                if (r, guard_y) in walls_locations or (r, guard_y) in guards_locations:
                    break
                marked[r][guard_y] = 1
            # right
            for c in range(guard_y+1, COLS):
                if (guard_x, c) in walls_locations or (guard_x, c) in guards_locations:
                    break
                marked[guard_x][c] = 1
            # left
            for c in range(guard_y-1, -1, -1):
                if (guard_x, c) in walls_locations or (guard_x, c) in guards_locations:
                    break
                marked[guard_x][c] = 1
        num_marked = 0
        for r in range(ROWS):
            for c in range(COLS):
                if marked[r][c] == 1:
                    num_marked +=1
        return m*n - num_marked - len(guards)-len(walls)
