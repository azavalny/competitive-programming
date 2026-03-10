class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        stars and bars problem where we have maximum limit stars between 2 bars
        stars = candies
        bars = 3 children

        n + k-1 choose k-1 where k=3 give syou all possible ways without limit restriction

        inclusion exclusion principle:
            valid = total - invalid singles + pairs - triples

            invalid = set one child at a time to limit:
                        compute 3*(n-limit+1) choose 2
                        
                        e.g. 3* 4choose 2 = 18 = 
                        n=5, limit=2
                        __ ___ ___
                        3   
                            n=2
                            k=3
                            2+3-1 = 5-2+1 choose 2
                            n + k-1 choose k-1
                    
                        ___ ___ ___ n=5
                         1   1   1
                        2+3-1 choose 3-1

            = 3*(n-limit+1) choose 2
        
        what if limit == n return total ways

        n = 4
        limit = 1, so we have to give each child 2 for the invalid case
            n=2
            k=3
            2+3-1 choose 2 = 4 choose 2
            *3 = 18
        6 choose 2 = 15
        15 - 18

        n=4, limit=1, k=3
        1 + 1 = 2
        n=2, limit=1, k=3

        **|**|*
        7c2 = n + k-1 choose k-1 where n = 5

        ||

        """
        def comb2(n):
            candies = n-2 # because we added 2 bars/children
            if candies < 0:
                return 0
            return math.comb(n, 2)
        total = comb2(n+2)
        invalid_limit = limit+1
        singles =  3*comb2(n-invalid_limit + 2)
        pairs = 3*comb2(n-2*invalid_limit + 2) # give 2 children limit + 1 how much left
        triples = comb2(n-3*invalid_limit + 2)# give each children limit + 1 how much left
        return total - singles + pairs - triples