class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        numCounts = Counter(nums)
        threshold = len(nums)//3
        sol = []
        for n, count in numCounts.items():
            if count > threshold:
                sol.append(n)
        return sol