class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        return 1 indexed
        nums is sorted
        O(1) space - no hash table

        [2, 7, 11, 15] target = 9
         l
            r
        15+2=13
        11+2=13
        7+2 = 9
        """
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1