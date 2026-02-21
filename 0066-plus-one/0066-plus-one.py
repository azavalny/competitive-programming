class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        get last digit and if its 9:
            
        otherwise increment by 1 and replace last value in array

       9 9
        +1
        for each digit from right:
            last_digit = digits[i]
            if last_digit == 9:
                carry = 0
                append [0]
        reverse at end
        """
        sol = []
        carry = 1
        for r in range(len(digits)-1, -1, -1):
            new_sum = digits[r] + carry
            last_digit = new_sum % 10
            carry = new_sum //10

            sol.append(last_digit)
        if carry > 0:
            sol.append(carry)
        sol.reverse()
        return sol