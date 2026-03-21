class Solution:
    def isUgly(self, n: int) -> bool:
        """
        keep dividing by 2, 3, 5 until you get 1 otherwise false
        """
        # negatives are not primes
        if n <= 0:
            return False
        for p in [5, 3, 2]:
            while n%p == 0:
                n = n//p
        if n == 1:
            return True
        return False