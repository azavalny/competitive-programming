class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        """
        max (y_i + y_j + y_k)   such that x_i, x_j, x_k distinct
        if not at least 3 distinct values of x return -1


        sort y values (with their x counterparts) and pick top y values where x's are distinct for i, j, k (keep looping until end)

        x = 3 1 1 2 2
        y = 6 5 4 3 2 (sorted)
            i 
              j
                  k
        6 + 5 + 3 = 14

        x = 1 1 1 2 3
        y = 6 5 4 3 2 (sorted)
            i
                  j
                     k
        6 + 3 + 2 = 11

        x = 1 3 3 2 3
        y = 6 5 4 3 2 (sorted)
            i
              j 
                  k
        6 + 5 + 3 = 15
        """
        pairs = list(sorted(zip(x, y), key=lambda x: x[1], reverse=True))
        i, j = 0, 1
        sol=pairs[0][1] # chose i as first
        usedXs = {pairs[0][0]}
        while j < len(pairs):
            if pairs[j][0] not in usedXs:
                sol += pairs[j][1]
                usedXs.add(pairs[j][0])
                break
            j+=1
        if len(usedXs) != 2:
            return -1
        k = j + 1
        while k < len(pairs):
            if pairs[k][0] not in usedXs:
                sol += pairs[k][1]
                usedXs.add(pairs[k][0])
                break
            k+=1
        if len(usedXs) != 3:
            return -1
        return sol