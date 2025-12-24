class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            sol[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            sol[i] *= suffix
            suffix *= nums[i]
        return sol