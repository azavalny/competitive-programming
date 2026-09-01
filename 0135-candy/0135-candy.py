class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        start new child with 1
            (while checking boundary conditions)
            if child i > child i+1 or if child i > child i-1, i should have 1 more
        return sum(candies) or keep track of running sum for O(1) space

ratings:   [1,0,2]
candies:    2 1 2

ratings:   [1,2,2]
candies:    1 2 1


        [1, 3, 2, 1]
candies: 1  3  2  1

        [3, 4, 2, 1]
candies: 1  3  2  1

        [1, 4, 1, 1]
candies: 1  2  1  1
heap  

initialize all to 0
heap (ratings[i], index)
    each child has one more than largest candies size of neighbors (assuming they're smaller)

[0, 0, 0]
[(0, 1), (1, 0), (2, 2)]
0 1
[0, 1, 0]
[(1, 0), (2, 2)]
1 0
[1, 1, 0]
[(2, 2)]
2 2
Output
3
Expected
5
        """
        heap = [(val, idx) for idx, val in enumerate(ratings)]
        heapq.heapify(heap)

        candies = [0]*len(ratings)
        while heap:
            curRating, i = heapq.heappop(heap)
            leftNeighborCandy, rightNeighborCandy = 1, 1
            # is either neighbor larger?
            l = max(0, i-1)
            if curRating > ratings[l]:
                leftNeighborCandy = max(1, candies[l]+1)
            r = min(i+1, len(ratings)-1)
            if curRating > ratings[r]:
                rightNeighborCandy = max(1, candies[r]+1)
            candies[i] = max(leftNeighborCandy, rightNeighborCandy)
        return sum(candies)