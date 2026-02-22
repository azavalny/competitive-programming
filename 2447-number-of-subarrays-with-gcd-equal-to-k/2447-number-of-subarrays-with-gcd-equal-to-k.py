class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        """
        # subarrays where GCD of subarray == k

        gcd(a, b, c) = gcd(gcd(a, b), c) associative

        note: for [4] gcd([4]) = gcd([4], 0) = 9

        [9,3,1,2,6,3], k = 3

        gcd(9, 3) = 3
        gcd(3, 1) = 1 < k will never increase
        gcd(1, 2) = 1
        gcd(1, 6) = 1
        gcd(1, 3) = 1

        so we should shrink the window

        [9, 3, 1, 2, 6, 3]
                  i
        gcd(2, 6) = 2 < k will never increase
        gcd(6, 3) = 3
        gcd(3, 0) = 3

        [9, 6, 3, 1]


        [4, 3]

        [4] gcd(4, 0) = 4
        [3] gcd(3, 0) = 3
        [4, 3] gcd(4, 3) = 1

        create hashmap of each element gcd value: count
        [9,3,1,2,6,3,3] k =3
                   i
        [{9: 1}, {3: 2}, {1:3}, {1:3, 2:1}, {1:3, 2:2, 6:1}, {1: 3, 2:2, 3: 2}, {1: 3, 2:2, 3: 3}]

                    gcd([9,3,1])=1
                    gcd([3,1]) =1
                    gcd([1]) =1

                    gcd([9, 3, 1, 2]) = 1
                    gcd([3, 1, 2]) = 1
                    gcd([ 1, 2]) = 1
                    gcd([2, 0]) = 2

                    gcd([9, 3, 1, 2, 6]) = 1
                    gcd([3, 1, 2, 6]) = 1
                    gcd([ 1, 2, 6]) = 1
                    gcd([2, 6]) = 2
                    gcd(6, 0) = 6
                    gcd([6, 1, 2]) = gcd(6, 1) = 1
                    gcd([6, 2]) = 2

                    gcd([9,3,1,2,6,3]) = 1
                    gcd([3, 1, 2, 6, 3]) = 1
                    gcd([ 1, 2, 6, 3]) = 1
                    gcd([2, 6, 3]) = 1
                    gcd([ 6, 3]) =3
                    gcd([3, 3]) = 1

        find gcd of each subarray
        check all gcds of subarrays ending at i and the counts
        """
        GCD = [{} for i in range(len(nums))]
        def gcd(a, b):
            if a < b:
                a, b = b,a
            while b > 0:
                a, b = b, a%b
            return a
        for i, n in enumerate(nums):
            GCD[i][n] = 1
            if i == 0:
                continue
            for gcdval, count in GCD[i-1].items():
                new_gcd = gcd(gcdval, n) # gcd(9, 3) = 3
                
                GCD[i][new_gcd] = GCD[i].get(new_gcd, 0)
                GCD[i][new_gcd] += GCD[i-1].get(gcdval, 0)
        sol = 0
        for hashmap in GCD:
            for key, val in hashmap.items():
                if key == k:
                    sol += val
        return sol