class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        35433
            i

        odd = last character (right pointer) is not divisible by 2
        """
        right = len(num)-1
        while right >= 0:
            rightInt = int(num[right])
            if rightInt%2 != 0:
                return num[:right+1]
            right-=1
        return ""

        # 10^5 digits can't be converted to int
        # num = int(num)
        # while num > 0:
        #     right = num%10
        #     if right%2 != 0:
        #         return str(num)
        #     num = num//10
        # return ""