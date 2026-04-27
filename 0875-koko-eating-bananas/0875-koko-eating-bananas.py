class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        return k (minimum eating speed of bananans/hr)
        each hour from 0 to h:
            eats k bananas from some pile[i] (all if less than k)

        [3, 6, 7, 11] h=8

        binary search from k=1 to k=max(piles) such that sum(math.ceil(pile[i]/k)) <= h

        for k=1 to max(piles):
            k = middle
            if hours <= h try smaller k otherwise do bigger k
        """
        l, r = 1, max(piles)
        k = 1

        while l <= r:
            k = l + (r-l)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                r = k -1
            else:
                l = k + 1
        return l