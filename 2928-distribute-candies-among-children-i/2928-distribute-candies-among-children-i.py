class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
            n=5 limit = 2
            (0, 0, 0)
            (1, 0, 0)
            (1, 1, 0),
            ...
            (1, 2, 2)
            (2, 1, 2)
            (2, 2, 1)

            for i from 0 to limit+1:
                for j from 0 to limit+1:
                    k = n - i - j
                    if 0 <= k <= limit:
                        sol +=1
        """
        sol = 0
        for i in range(0, limit+1):
            for j in range(0, limit+1):
                k = n - i - j
                if 0 <=k and k <= limit:
                    sol +=1
        return sol