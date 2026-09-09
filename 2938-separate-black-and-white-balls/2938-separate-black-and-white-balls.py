class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        1-black, 0-white

        min number of adjacent swaps to group all black to right

        in sorting its easier to move right to left, so lets do the same using two pointers
        everything left of left is 0's


        101100
          l
             r
1 + 3 +3 = 7
    increment right forward until end
        if right is 1: continue
        if right is 0: add r-l to sol, move left by 1
        """
        l = 0
        sol=0
        for r in range(len(s)):
            if s[r] == "1":
                continue
            else:
                sol += r-l
                l+=1
        return sol