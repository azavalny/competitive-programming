class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        max water container = max area bounded by lower height of two ends
            area[l, r] = (r-l)*min(height[l], height[r])

        [1, 8, 6, 2, 5, 4, 8, 3, 7]
         l
                                 r   

        always move pointer that points to the lower line
        
        """
        maxArea = 0
        l = 0
        r = len(height)-1

        while l < r:
            maxArea = max(maxArea, (r-l)*min(height[l], height[r]))
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxArea