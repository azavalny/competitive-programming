class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        from each nums[i] make range of values you can reach 
        find farthest you can reach max(i + nums[i]) and set right to it and left to right
        """
        sol=0
        l, r, = 0, 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1): # set farthest
                farthest = max(farthest, i + nums[i])
            l = r +1
            r = farthest
            sol+=1
        return sol