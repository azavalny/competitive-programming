class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        n = sum of distinct powers of 3
        
        y is power of three if log_3(y) gives integer

        n = x + y + z + ...

        1, 3, 9, 27, 81                                                            
        """
        res = False
        arr = [3**i for i in range(int(math.log(n, 3))+1)]

        def dfs(index, curSum):
            nonlocal res
            if index == len(arr):
                if curSum == n:
                    res = True
                return

            if curSum > n or res == True:
                return False
            
            dfs(index + 1, curSum)
            dfs(index + 1, curSum + arr[index])
        dfs(0, 0)
        return res