class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        sol=0
        # outer loop pins largest then use two pointer to find pairs and bank right-left triples
        for i in range(len(nums)-1, 1, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    sol+= r-l
                    r-=1
                else:
                    l+=1
        return sol