class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        ramp = two numbers where right is greater, width = j-i
        
        max width of a ramp in nums

        eliminating a left candidate if max value left of it is les than it
            preprocessing step of using a maxRight array

nums       [6, 0, 8, 2, 1, 5]
               L         
                           R
            compare nums[L] <= maxRight[L]:
                sol +=1
                shift right
            else:
                shift left

maxRight    8  8  8  5  5  5 
        
        at each step we know result is at least that value as we shift right

        """
        maxRight = [0]*len(nums)
        prevMax = 0
        i=len(nums)-1
        for n in reversed(nums):
            maxRight[i] = max(n, prevMax)
            prevMax = maxRight[i]
            i-=1
        
        sol=0
        l = 0
        for r in range(len(nums)):
            while nums[l] > maxRight[r]:
                l+=1
            sol = max(r-l, sol)
        return sol