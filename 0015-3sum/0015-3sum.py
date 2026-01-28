class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort input array to make it nlogn instead of n^3 and run two sum ii sorted on each negative value of n

        nums[i] + nums[j] + nums[k] == 0
        nums[i] + nums[j] == -nums[k]

        sorted([-1, 0, 1, 2, -1, -4])
    ==>        [-4, -1, -1, 0, 1, 2]

        for n in sorted(nums):
            return two_sum_ii(-n)

        [-2, 0, 1, 1, 2]
    -2        l       r 

        """
        sorted_nums = sorted(nums) #nlogn
        sol = []
        seen = {}

        def two_sum_ii(k, i):
            l = i+1
            r = len(sorted_nums)-1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == k:
                    if str([sorted_nums[i], sorted_nums[l], sorted_nums[r]]) not in seen:
                        sol.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                        seen[str([sorted_nums[i], sorted_nums[l], sorted_nums[r]])] = True
                    l+=1
                    r-=1
                elif sorted_nums[l] + sorted_nums[r] > k:
                    r-=1
                else:
                    l+=1

        for i, n in enumerate(sorted_nums): #n^2
            two_sum_ii(-n, i) #n
        return sol