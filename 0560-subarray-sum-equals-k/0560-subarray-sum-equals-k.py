class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        prefix[j] - prefix[i] == k
        prefix[j] -k = prefix[i] 

        does the complement of prefix[j] -k exist?
        """
        table = defaultdict(int, {0: 1}) #{ curSum: counts}
        sol = 0
        curSum = 0

        for n in nums:
            curSum +=n
            sol += table[curSum - k] # increment solution w/ frequency if curSum-k exists else increment by 0 if not
            table[curSum] +=1
        return sol
