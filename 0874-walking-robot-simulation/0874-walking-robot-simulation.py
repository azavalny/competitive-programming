class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        start (0, 0) dir = north

        -2: turn left 90 degrees
        -1: turn right 90 degrees
        move forward k steps unless stopped by obstacle


        Euclidean distance = sqrt((x2-x1)^2 + (y2-y1)^2)
        from origin = sqrt(x2^2 + y2^2)

        there can be obstacle at 0,0 so robot initially ignores

        dirs = (0, 1), (1, 0), (0, -1), (-1, 0)

        loop through commands:
            move robot:
                if -2: 
                    (dir + 3)%4
                if -1:
                    (dir +1)%4
                else:
                    for i in range(k):
                        if current coord not in obstacles: #can be O(1) of obstacles is hashset
                            coord[0] += dx
                            coord[0] += dy
                        else:
                            break and go back to previous position and go to next instruction
            update solution if newmax found
        
        
        important edge case: obstacle at (0,0)
        instructions: 1, -2, -2, -2, 10
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0 # North initially
        sol = 0

        obs = set()
        for x, y in obstacles:
            obs.add((x, y))

        startx, starty = 0, 0
        for command in commands:
            if command == -2:
                direction = (direction + 3)%4
            elif command == -1:
                direction = (direction + 1)%4
            else:
                for i in range(command):
                    newX = startx + dirs[direction][0]
                    newY = starty + dirs[direction][1]
                    if (newX, newY) in obs:
                        break
                    startx, starty = newX, newY
            sol = max(sol, startx**2 + starty**2)
        return sol