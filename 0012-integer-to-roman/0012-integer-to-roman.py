class Solution:
    def intToRoman(self, num: int) -> str:
        """
        sol = ""
while x > 0:
    maxDecimal +=1
    x = x//10
num//(10^maxDecimal)

or 

        3749
= 3000 + 700 + 40 + 9
3000 = 3*M
700 = 500 + 2*C
40 = XL
9 = IX

                e.g. 80000 = MMM
                    4000 = CM
                    3100 = MMM
                    100 = C
                    MM CM MMM C

                    800 = D
                    300 = CCC
                
                40 = XL

        58
        50 L
        8  V
        3

        for each value (digit*10^(decimal place)) for each digit:
            if value starts with 4 or 9:
                use subtractive form hashmap
            else:
                symbol of max value

                e.g. 3000
                currentMaxLessThanN
                for each value in map:
                    is value < 3000

        """
        sol = ""
        roman = {
1: "I",
5: "V",
10: "X",
50: "L",
100: "C",
500: "D",
1000: "M"
        }
        subtractive_form = {
            4: "IV", 9: "IX", 
            40: "XL", 90: "XC",
            400: "CD", 900: "CM"
        }
        """
        49 => 40

        """
        def largest_value_less_than_current(x: int, hashmap) -> int:
            currentMaxLessThanX = 0
            for key, value in hashmap.items():
                if key <= x:
                    currentMaxLessThanX = max(currentMaxLessThanX, key)
            return currentMaxLessThanX

        while num > 0:
            first_digit = int(str(num)[0])
            if first_digit == 4 or first_digit == 9:
                largest = largest_value_less_than_current(num, subtractive_form)
                sol += subtractive_form[largest]
                num -= int(largest)
            else:
                largest = largest_value_less_than_current(num, roman)
                sol += roman[largest]
                num -= int(largest)
        return sol