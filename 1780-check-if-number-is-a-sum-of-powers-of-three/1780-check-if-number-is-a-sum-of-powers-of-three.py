class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        n = sum of distinct powers of 3
        
        y is power of three if log_3(y) gives integer

        n = x + y + z + ...

        1, 3, 9, 27, 81                                                            
        """
        res = False

        def dfs(i, curSum):
            nonlocal res
            if i == int(math.log(n, 3))+1:
                if curSum == n:
                    res = True
                return

            if curSum > n:
                return False
            
            dfs(i + 1, curSum) # skip
            dfs(i + 1, curSum + 3**i) # use
        dfs(0, 0)
        return res