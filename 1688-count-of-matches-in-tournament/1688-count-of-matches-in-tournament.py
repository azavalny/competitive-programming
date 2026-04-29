class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        even: n/2 matches n/2 advance
        odd: (n-1)/2 matches (n-1)/2 + 1 advance

        return sum of matches until you get to 2 teams remaining

        while n > 1:
            if n is even:
                matches += n/2
                n = n/2
            else:
                matches += (n-1)/2 
                n = (n-1)/2 + 1
        """
        matches = 0
        while n > 1:
            if n%2==0:
                matches += n/2
                n = n/2
            else:
                matches += (n-1)/2
                n = (n-1)/2 + 1
        return int(matches)