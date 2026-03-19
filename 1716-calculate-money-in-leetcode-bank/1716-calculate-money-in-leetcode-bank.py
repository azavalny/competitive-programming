class Solution:
    def totalMoney(self, n: int) -> int:
        """
        M: 1
        T-S: 1 + prev

        track prev monday, prev day

        OR
        n//7 = weeks_passed
        n%7 = day end off at last week


        sum increases by 7 each week
        if weeks_passed != 0
            total = 28 + (n//7 - 1)* 7

        to get last week:
        weeks_passed +1 and increment it n%7 -1 times

        M, T, W, T, F, S, S
        1, 
        """
        total  = 0
        weeks_passed = n//7
        days_of_last_week = n%7
        # values*(first+last)//2
        first = 28
        last = first + (weeks_passed-1)*7
        total += weeks_passed*(first + last)//2

        if days_of_last_week%7 != 0:
            monday_last_week = weeks_passed + 1
            total += monday_last_week
            for i in range(days_of_last_week-1):
                monday_last_week +=1 
                total += monday_last_week
        return total