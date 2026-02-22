class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        return largest string x such that it divides both str1 and str2

        str2 can be larger than str1

        compare min(len(str1, str2)) * O(m + n)

        ABABAB
        ABAB
        
        """
        if len(str1) > len(str2): # str1 < str2
            str1, str2 = str2, str1
        
        cur = list(str1)
        for i in range(len(str1)-1, -1, -1):
            curGCDLen = i + 1

            if len(str2) % curGCDLen != 0 or len(str1)%curGCDLen != 0:
                cur.pop()
                continue
            else:
                string = "".join(cur)
                factorStr1, factorStr2 = len(str1)// curGCDLen, len(str2)//curGCDLen

                str1Full = factorStr1 * string
                str2Full = factorStr2 * string

                if str1Full == str1 and str2Full == str2:
                    return string

                cur.pop()
        return ""
            
        