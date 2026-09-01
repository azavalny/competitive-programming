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
        n = len(ratings)
        candies = [1] * n

        # Pass 1: satisfy the left rule (higher than smaller left neighbor)
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Pass 2: satisfy the right rule without breaking the left rule
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)