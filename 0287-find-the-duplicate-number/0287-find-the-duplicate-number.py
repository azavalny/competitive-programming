class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        find duplicate number 
            without modifying nums
            constant extra space so in place
        [1,3,4,2,2] => [1,2,2, 3, 4]
        brute force O(n^2) sort then linear scan while keeping track of previous
        
        sort then run binary search on answer space min of nums to max of nums

        
        """
        nums.sort()
        prev = 0
        for n in nums:
            if n == prev:
                return n
            prev = n
        