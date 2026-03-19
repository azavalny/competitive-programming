class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        if starts with odd
        3, 4, 5, 6, 7 = (7 - 3) //2 + 1

        if starts with even:
        10-8 = 2//2 = 1

        13, 14, 15, 16, 17
        """
        if low%2 == 0:
            if high %2 == 0:
                return (high - low)//2
            else:
                return (high-low)//2 + 1
        else:
            return (high-low)//2 + 1