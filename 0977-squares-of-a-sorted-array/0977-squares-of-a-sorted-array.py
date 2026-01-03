class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        write = n - 1

        while l <= r:
            left = nums[l]
            right = nums[r]
            if abs(left) > abs(right):
                res[write] = left * left
                l += 1
            else:
                res[write] = right * right
                r -= 1
            write -= 1

        return res

        """
nums = [-4, -1, 0, 3, 10]
                l
                r
                w
        [     1  9  16  100]

        """ 