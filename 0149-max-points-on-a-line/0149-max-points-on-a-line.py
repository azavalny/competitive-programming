class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        idea 1:  O(n^2) brute force
        for each point:
            create hash table
            for each other point:
                calculate slope between point and other point
                if it appears in hash table increment it
            update solution with max value of hash table

        (1,1) {inf: 2, 2: 2, 1/2 : 3, 0 : 2} max is 3
        """
        sol = 0
        for i in range(len(points)):
            table = {} # slope : count
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                slope = 0
                if y2 - y1 == 0:
                    slope = 0
                elif x2 - x1 == 0:
                    slope = float("inf")
                else:
                    slope = (x2 - x1) / (y2 - y1)
                if slope in table:
                    table[slope] +=1
                else:
                    table[slope] = 1
                sol = max(sol, table[slope])
        return sol+1 # to count source