class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        color = 2
        sr, sc = 1,1
        [2,2,2]
        [2,2,0]
        [2,0,1]
        

        stack = [] append to right pop from right

        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            x + dir[0], y + dir[1]

        if new cell matches starting color:
            push to stack if coordinate not seen



        [0,0,0]
        [0,0,0]
        """
        color_of_source = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        stack = [(sr, sc)]
        seen = set()

        while stack:
            curR, curC = stack.pop()
            seen.add((curR, curC))
            
            if image[curR][curC] == color_of_source:
                image[curR][curC] = color

                # get valid neighbors w/ boundary check
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR = curR + dr 
                    newC = curC + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and not (newR, newC) in seen:
                        stack.append((newR, newC))
        return image