class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        idea 1: build reversed integer then compare at end to x

        idea 2: two pointer loop through ends and return False if L != R

        negative numbers cannot be palindrome for this problem
        while x > 0:
            last_digit = x%10
            reversed digit = reversed_digit*10 + last_digit
            x //10

        1 2 1
          10^0 + 2*10^1 + 1*10^2
        
            5   3 3
reversed:   335 33 3
last_digit:  5   3 3
        
        """
        reversedNum = 0
        x_copy = x
        while x_copy > 0:
            last_digit = x_copy%10
            reversedNum = reversedNum*10 + last_digit
            x_copy = x_copy//10

        return reversedNum == x