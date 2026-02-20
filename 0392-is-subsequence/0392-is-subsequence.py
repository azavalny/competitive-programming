class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        is s a subsequence of t when characters can be removed from t to get s without changing order of s's chars
        
        can't use frequency map bc not anagram problem

        abc     ahbgdc
          i
                     j


        axc     ahbgdc
         i
                      j

        for every character in t
        """
        i = 0 # pointer for s
        for c in t:
            if i < len(s) and c == s[i]:
                i+=1
                if i == len(s): #have seen every character in s
                    return True
        return i == len(s)