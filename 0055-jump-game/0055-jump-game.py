class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        queue (indexes): [0]

        [3,2,1,0,4]
                 l
               r
farthest: 

l=r+1
r=farthest (before out of bounds)
        """
        l, r = 0,0
        farthest = 0
        while l <= r and r < len(nums):
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l=r+1
            if r == len(nums)-1:
                return True
            r = min(farthest, len(nums)-1)
        return False