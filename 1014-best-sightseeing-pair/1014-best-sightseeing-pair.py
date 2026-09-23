class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        value of ith sightseeing spot

        score of pair of spots is sum of values + i-j (minus distance between them)

        find max score of a pair of sightseeing spots

        l=0,r=1

        [8, 1, 5, 2, 6]
        l
                  r
        8,1 = 9-1 = 8
        8,5 = 8+5-2=11
        1,5=6-1=5
        1,2=3-2=1
        1,6=7-4=3
        5,6=11-2=9
        2,6=8-1=7

        brute force = try every pair in O(n^2) and update maxScore

        if v[r+1] is greater than v[r], move r
        elif decrease l while l < r-1 (dont if v[l]> v[r+1])
        else move r

        update maxScore

        if r reaches end, keep trying each l until end

        [1, 2]
        1,2=3-1=2

        [1, 2, 3, 4]
               l
                  r
        3,4=7-1=6
        [4, 3, 2, 1]
            l
               r
        4,3=7-1=6
        4,2=6-2=4
        3,2=5-1=4

        [8, 1, 5, 2, 100, 100]
         l
                           r
        8,1=9-1=8
        8,5=11
        1,5=6-1=5
        1,2=3-2=1
        1,100=101-3=98
        5,100=105-2=103
        2,100=102-1=101
        2,100=102-2=100
        100,100=200-1=199

        [100, 1, 5, 2, 99]
         l
                       r
        100,1=101-1=100
        100,5=105-2=103

        [100, 1, 1, 1, 1................10^3, 100, 1000]
                                               l
                                                     r
        1, 101=102-1=101
        1, 1000=10001-2=999
        100, 1000=1100-1=1099

        [100, 1, 1, 1, 1,99, 99, 1,1,5]
                          l
                                     r
        100, 1 = 101-1=100
        100, 99=199-5=194


        [100, 1, 1, 1, 1................10^3, 100, 1000]
                 i
curr_max=101-1=100-1=99

        r=1
        for each r:
            sol = max(sol, V[r] + curr_max)
            curr_max = max(V[r]-1, curr_max-1)

        """
        sol=0
        prev_max=0
        for r in range(len(values)):
            sol = max(sol, values[r] + prev_max)
            prev_max = max(values[r]-1, prev_max-1)
        return sol