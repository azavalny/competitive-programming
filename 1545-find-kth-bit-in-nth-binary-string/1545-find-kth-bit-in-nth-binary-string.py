class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        S_1=0
        S_i = S_i-1 + 1 + reverse(invert(S_i-1))

        return kth bit in S_n

        k can be 2^20 = 10^6

        n=3, k=1
        S_3 = S_2 + 1 + reverse(invert(S_2))
    =   011 + 1 + reverse(invert(011))
    =   0111 + reverse(100)
    =   0111 + 001
    =   0111001, k=1 => 0

        recursion + memoization to optimize?

        S_4 = S_3 + 1 + reverse(invert(S_3))

        iterative:
            for i from 1 to n:
                S_i = S_i-1 + 1 + reverse(invert(S_i-1))
        
        invert = XOR binary value with 1 (always flips bit)
        """
        def digit_reverse(digit: str)->str:
            return str("".join(list(reversed(digit))))
        
        def digit_invert(digit: str)->str:
            output_string = ""
            for d in digit:
                if d == "1":
                    output_string += "0"
                else:
                    output_string += "1"
            return output_string

        S_n = "0"
        S_prev = S_n
        for i in range(1, n):
            S_n = S_prev + "1" + digit_reverse(digit_invert(S_prev))
            S_prev = S_n
        return S_n[k-1]