class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [7,1,5,3,6,4] 
           L
                   R
        
        Move left to right when prices[r] < prices[l] bc we want long

        [7,6,4,3,1] <- monotonically decreasing prices have no transactions

        invariant: 

        """
        sol = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            sol = max(sol, prices[r]-prices[l])
        return sol
        