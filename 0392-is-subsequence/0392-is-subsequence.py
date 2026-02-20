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
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j +=1
        return i == len(s)