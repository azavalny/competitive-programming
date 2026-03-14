class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        b^2 + a^2 = c
        b = sqrt(c -a^2)  set = {sqrt(c -a^2)} }
        
        check every a from a to sqrt(c):
            have we seen sqrt(c -a^2) in set:
                return True
            add to set

        c=5, a and b < sqrt(5)
        a, b = 0, 1, 2

        b's = {0, 1, 2}
        a = 2
        b = 5-2^2 = 1
        """
        b = set()
        for i in range(int(math.sqrt(c))+1):
            b.add(i)
        for a in range(int(math.sqrt(c))+1):
            if math.sqrt(c - a**2) in b:
                return True
        return False