"""
store new points with duplicates allowed and differentiated so (i, (x, y))

count((x, y)) => number of ways to form axis aligned square with (x, y) and 3 other points
    axis aligned square = edges are same length and parallel or perpendicular to x and y axis

(x,y)
for every stored point (x2, y) on same horizontal line:
    skip if same point
                              left      up/down       top/bottom left
    square above = counts of (x2, y) * (x, y + d) * (x2, y +d) for 4 corners
    square below = counts of (x2, y) * (x, y-d) * (x2, y-d)

query (3, 2)
horizontal (5, 2)
d = 5 - 3
above: (3, 4) and (5, 4)
below: (3, 0) and (5, 0)

counts of every point = {(x,y):count}

"""
from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.counts[(point[0], point[1])] +=1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        horizontal_values = []
        sol =0
        for x_n, y_n in self.counts.keys():
            if y_n == y:
                if x_n == x: # 4 coordinates
                    continue
                d = abs(x - x_n)
                square_above = self.counts.get((x_n, y), 0)*self.counts.get((x, y + d), 0)*self.counts.get((x_n, y+d), 0)
                square_below = self.counts.get((x_n, y), 0)*self.counts.get((x, y - d), 0)*self.counts.get((x_n, y-d), 0)
                sol = sol + square_above + square_below
        return sol


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)