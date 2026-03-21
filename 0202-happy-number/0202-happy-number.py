class Solution:
    def isHappy(self, n: int) -> bool:
        """
        2 = 2^2 = 4^2 = 16 = 1^1 6^2 = 36 = 3^2 6^2 = 3^2 2^2 4^2 = 29

        visited = {} to store sum of squares to check if seen

        slow, fast pointer idea no set
        while slow != 1:
            move slow do sum of squares
            move fast do sum of squares twice

            if slow == fast:
                return False
        """
        def sumOfSquares(n: int) -> int:
            total = 0
            while n > 0:
                total += (n%10)**2
                n = n //10
            return total

        slow, fast = n, n
        if n == 1:
            return True

        while slow > 1:
            print(slow, fast)
            slow = sumOfSquares(slow)
            fast = sumOfSquares(fast)
            fast = sumOfSquares(fast)

            if slow == 1:
                return True

            if slow == fast: # if fast reaches slow pointer then we detect cycle
                print("CYCLE DETECTED:", slow, fast)
                return False
        return True