class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        like the zip function

        a b    p q r s
          l
                 r
sol=apbq
append word1[l], append word2[r], increment both until either reaches end of array
        """
        sol=""
        l = 0
        r = 0
        while l < len(word1) and r < len(word2):
            sol += word1[l]
            sol += word2[r]
            l+=1
            r+=1
        if l < len(word1) -1:
            sol+= word1[l:]
        if r < len(word2) -1:
            sol += word2[r:]
        return sol
