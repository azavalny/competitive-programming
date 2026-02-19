class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        goal: min difference between highest and lowest of any k scores chosen

        [9, 4, 1, 7]  k =2
sorted= [1, 4, 7, 9] k =2
         ____
            ____
               ____

sorted= [1, 4, 7, 9] k =3
         _______
            _______

        min difference comes from k chosen scores as close to each other as possible which helps when sorted otherwise
        you'll have to have n^2
        """
        nums.sort()
        l = 0
        sol = float("inf")
        for r in range(k-1, len(nums)):
            sol = min(sol, nums[r] - nums[l])
            l+=1
        return sol