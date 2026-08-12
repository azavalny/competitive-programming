class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        cost per lemonade = $5
        have to store the bills you keep for future (hashmap)

        [5,5,5, 10,10,20]
                       i
{
5: 1
10: 2
20:
}

5 means no change needed just increment the 5

10:
    give back 5 if we cannot return False
    collect 10
20:
    1. give back 10 and 5
    else or all 5's
    else return False
return True
        """
        wallet = {5: 0, 10: 0, 20: 0}
        for payment in bills:
            if payment == 5:
                wallet[5] +=1
            elif payment == 10:
                if wallet[5] == 0:
                    return False
                else:
                    wallet[5] -=1
                    wallet[10] +=1
            else: #payment == 20
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -=1
                    wallet[5] -=1
                elif wallet[5] >= 3:
                    wallet[5] -=3
                else:
                    return False
        return True