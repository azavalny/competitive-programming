class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s2 contains a permutation of s1 when s1's characters are a subset of s2's characters

        e i d b a o o o contains ab?
        ___
          ___
            ___
              ___
                 ___

        slide window of size s1:
            is window's hash table of frequencies equal to s1's?
        """
        s1Freq = dict(Counter(s1))
        curWindow = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1) + 1):
            if curWindow == s1Freq:
                return True

            if i < len(s2) - len(s1):
                curWindow[s2[i]] -=1
                if curWindow[s2[i]] == 0:
                    del curWindow[s2[i]]

                curWindow[s2[i + len(s1)]] +=1

        return False