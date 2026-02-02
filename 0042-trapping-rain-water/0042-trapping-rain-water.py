class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]



        potential - height
        min(max_left[l], max_right[r]) - height

        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
   L= [0 0  1  1  2  2  2  2  2  3  3  3  3]
   R= [  3  3  3  3  3  3  3  2  2  2  1  0]

S = 6
        l_wall = r_wall = 0
        max_left = [0]*len(height)
        max_right = [0]*len(height)

        for i in range(len(height)):
            j = -i -1  #- indexes in python go backwards
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        sol = 0
        for i in range(len(height)):
            potential = min(max_left[i], max_right[i])
            sol += max(0, potential - height[i])
        return sol
        """

        l, r = 0, len(height)-1
        lMax,rMax=height[l],height[r]
        sol = 0

        while l < r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax, height[l])
                sol += lMax - height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                sol += rMax - height[r]
        return sol

