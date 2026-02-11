class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        length of longest substring where you can change at most k characters to make them the same letters

        A B A B      k = 2
        L
              R
diffChar0 1 1 2

        A A B A B B A   k=1
                L
                    R
diffChar0 0 1 1 2

        A B A B A k = 2
          L
              R

        A A B A     k = 0
        L
          R
        """
        sol = 0
        l = 0
        count = {}
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            
            while r - l + 1 - maxFreq > k:
                count[s[l]] -=1
                l +=1
            sol = max(sol, r - l + 1)
        return sol