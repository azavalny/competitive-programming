class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        sort([3,2,2,1]) ==> [1, 2, 2, 3] limit=3
                                l
                                   r
        greedy:

        """
        people.sort()
        sol = 0
        l = 0
        r = len(people)-1

        while l <= r:
            remain = limit - people[r] #limit - heaviest
            r-=1
            sol+=1
            if l <= r and remain >= people[l]:
                l+=1
        return sol