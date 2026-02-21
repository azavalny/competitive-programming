class Solution:
    def romanToInt(self, s: str) -> int:
        """

        12 = XII =  X + 2*I
        27 = XXVII = 2*X + V + 3*I

        IV = (5-1) = 4
        IX = (10-1) = 9
        XL = (50-10) = 40
        XC = (100-10) = 90
        CD = (500-100) = 400
        CM = (1000-100) = 900


        M CM XC IV = 1000 + 900 + 90 + 4

        map ={
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
        }

        for each number:
            check if i +1 is greater:
                sol += map[i + 1] - map[i]
            else:
                sol + map[i]
        """
        roman = {
"I":             1,
"V":             5,
"X":             10,
"L":             50,
"C":             100,
"D":             500,
"M":             1000
        }
        sol = 0
        i=0
        while i < len(s):
            if i < len(s)-1 and roman[s[i+1]] > roman[s[i]]:
                sol += roman[s[i+1]] - roman[s[i]]
                i+=2
            else:
                sol += roman[s[i]]
                i+=1
        return sol