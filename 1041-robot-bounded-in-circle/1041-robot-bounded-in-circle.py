class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        dir = north at (0,0) 

        dirs = N (0, 1), E (1, 0),S (0, -1),  W (-1, 0)

        G = go straight
        L = turn 90 degrees left
        R = turn 90 degrees right

        Performs instructions & repeats forever
        Return if robot goes in cycle:
            1. No G's only L or R

        idea 1: simulate robot moving on grid and return true if coordinate comes back that you've seen

        e.g. 
        GG = left and right 0
        GL = left is 1 and right is 0
        GR = left is 0 right is 1
        GLLG = left is 2 right is 0
        GLLR = left 2 righ 1
        GLLLL = 4 lefts right 0

        two lefts undo last move
        
        idea 2: condense consecutive Lefts and Rights to be one
        V
        idea 3: ignore G's just loop over rotations.IF you end on a different direction then you started then you know you'll do a cycle

        idea 4: robot stays in cycle at end:
            1. back at origin OR
            2. does not face north

        for each move:
            if move is left turn:
                dir = (dir + 3)%4
            elif move right turn
                dir +=1
            else:
                coord[0] += dir[0]*1
                coord[1] += dir[1]*1
        are we not back at (0,0) and is dir not North?
        """
        dirs = [(0, 1), (1, 0), (0, -1),  (-1, 0)]
        coord = [0, 0]
        direction = 0 # index of dirs array
        for move in instructions:
            print("START", move, coord, direction)
            if move == "L":
                direction = (direction + 3)%4
            elif move == "R":
                direction = (direction + 1)%4
            else:
                dx, dy = dirs[direction]
                coord[0] += dx
                coord[1] += dy
            print("END", move, coord, direction)
        print("#"*10)
        print("END", coord, direction)
        if coord == [0, 0] or direction != 0: # back at Origin or not North
            return True
        return False