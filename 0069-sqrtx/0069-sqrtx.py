class Solution:
    def mySqrt(self, x: int) -> int:
        """
        binary search on 0 to x to check if mid^2 > x

        mid^2 <= x is candidate for result and we want largest
        """
        l, r = 0, x
        sol = 0
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid > x:
                r = mid-1
            elif mid*mid < x: # greatest mid^2 less than x
                l = mid + 1
                sol  = mid
            else:
                return mid
        return sol
        