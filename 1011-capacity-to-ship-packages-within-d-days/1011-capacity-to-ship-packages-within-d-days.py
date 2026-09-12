class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        find smallest weight capacity st all weights shipped within d days

        number of ships to load under capacity

        run bin search capacity from max(weights) to sum(weights)
        
        if a capacity works, we dont have to search higher we can try lower
        if a capacity too small so will all weights less than will be

    weights: 1, 2, 3, 4, 5

        m=10    1, 2, 3, 4, + 5
        L=5
        R=15

        m=7     1, 2, 3, + 4 + 5
        L=5
        R=10-1
        """
        def canShip(capacity):
            ships, currCap = 1, capacity
            for w in weights:
                if currCap - w < 0:
                    ships +=1
                    currCap = capacity
                currCap -=w
            return ships <= days
        l, r = max(weights), sum(weights)
        sol = r

        while l <=r:
            capacity = l + (r-l)//2
            if canShip(capacity):
                sol = min(sol, capacity)
                r = capacity-1
            else:
                l = capacity + 1
        return sol
        