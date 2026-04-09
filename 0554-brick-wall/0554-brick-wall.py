class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        total width of each row same
        going through edge = multiple curSums across rows align
        do not include left and right boundary

        min number of crossed bricks after drawing vertical line
        = max number of rows with the same curSum

        """
        edges = Counter()

        for row in wall:
            i = 0
            for brick in row[:-1]:
                i += brick
                edges[i] +=1
        return len(wall) - (max(edges.values()) if edges else 0)