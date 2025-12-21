class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        current = 0
        for n in nums:
            current += n
            self.prefixSums.append(current)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSums[right]
        if left <= 0:
            leftSum = 0
        else:
            leftSum = self.prefixSums[left-1]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)