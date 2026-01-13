class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        strictly before and strictly after mean prefix[i-1] and suffix[i+1] which follow the formulas
        [1,  7,  3,   6,  5,   6]
        [1,  8,  11, 17,  22, 28]
        [28, 27, 20, 17,  11,  6]

        left sum is 0 if i == 0,  right sum is 0 if i == len(nums)

        """
        prefix = [sum(nums[:i+1]) for i in range(len(nums))]
        suffix = [sum(nums[i:]) for i in range(len(nums))]
        print(prefix, suffix)

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1