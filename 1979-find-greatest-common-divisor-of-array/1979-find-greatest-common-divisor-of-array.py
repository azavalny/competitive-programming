class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = max(nums), min(nums)
        while b > 0:
            a,b = b, a%b
        return a
    
    """
    gcd(8, 3) = gcd(3, 2) = gcd(2, 1) = gcd(1, 1) = 1
    """