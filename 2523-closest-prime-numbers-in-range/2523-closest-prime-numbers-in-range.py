class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """
        find 2 integers between (or equal) to left and right such that:
            1. they're both prime
            2. their difference is minimum (closest)

        return smallest num1 value if multiple pairs

        idea 1: use adjusted sieve algorithm to compute primes between left and right
            note: sieve returns in sorted order

        10, 19
sieve:  11, 13, 17, 19
find closest pair of primes starting from left:
11 - 13 = 2
13 - 17 = 4
19 - 17 = 2 <= num1 != currentMin and num1 of currentMin


            10 11 12 13 14 15 16 17 18 19
is_prime    F  T   F  T  F  T  F T  F  T

==>         11, 13, 17, 19
                     i
                        i+1
curMinDiff = 2
sol = [11, 13]
        """
        is_prime = [True]*(right+1)   #[0, right]
        if left < 2:
            left = 2
        if right < 2:
            return [-1, -1]

        for i in range(2, int(math.sqrt(right))+1):
            if is_prime[i]:
                for mult in range(i*i, right + 1, i):
                    is_prime[mult] = False

        primes = [i+left for i, x in enumerate(is_prime[left:right+1]) if x]
        curMinDiff = float("inf")
        sol = [-1, -1]        
        for i in range(len(primes)-1):
            if primes[i+1] - primes[i] < curMinDiff:
                curMinDiff = primes[i+1] - primes[i]
                sol = [primes[i], primes[i+1]]
        return sol