class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        a b c a b c b b
                      l
                       r
        increment r for every character
        once duplicate is found:
            move left pointer right until duplicate is gone

        b b b b b
              L
                R 
        p w w k e w
              L
                  R 

        """
        sol = 0
        l = 0
        curSet = set()
        for r in range(len(s)):
            while s[r] in curSet:
                curSet.remove(s[l])
                l+=1
            curSet.add(s[r])
            sol = max(sol, r-l+1)
        return sol