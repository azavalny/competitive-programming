class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        {0: evenPrefixCount, 1: oddPrefixCount}
            count subarrays ending at each element
        
        from even sum if we remove odd prefixes we get odd
        from odd sum if we remove odd prefixes we get even
        even - odd = odd
        odd - odd = even

        add how many previous prefixes have the opposite parity to form an odd-sum

        possible with dp using odd and even count
        1, 3, 5
curSum  1  4  9
odd     1  1  2
even    1  2  2
sol     1  2  4
        """
        oddCount = 0
        evenCount = 1
        sol = 0
        curSum = 0

        for n in arr:
            curSum +=n
            if curSum%2 == 0:
                sol += oddCount
                evenCount +=1
            else:
                sol += evenCount
                oddCount +=1
        return sol%(10**(9) + 7)