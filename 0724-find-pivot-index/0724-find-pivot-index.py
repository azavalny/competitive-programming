class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, x in enumerate(nums):
            # Check if left sum equals right sum
            # (total_sum - left_sum - x) is the sum of elements to the right
            if left_sum == (total_sum - left_sum - x):
                return i
            left_sum += x
            
        return -1