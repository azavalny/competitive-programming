class Solution:
    def countPrimes(self, n: int) -> int:
        """
        initialize is_prime array and set 0 to false
        run sieve algorithm
        """
        if n <=1:
            return 0
        is_prime = [True]*n
        is_prime[0] =  False
        is_prime[1] = False

        for i in range(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for multiple in range(i*i, n, i):
                    is_prime[multiple] = False
        return sum(is_prime)