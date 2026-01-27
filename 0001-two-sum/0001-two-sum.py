class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2, 7, 11, 15] t=9

        {
            7: 0

        }
        """
        diffs = {} #diff: index
        for i, n in enumerate(nums):
            if target - n in diffs:
                return [diffs[target-n], i]
            diffs[n] = i