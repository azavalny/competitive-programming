class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [1, 2, 3, 4, 5, 6, 7]
            j

        sol 1:
            run k times: O(nk) = O(n^2)
                store last element
                shift every element to right O(n)
                first element = original last element

        sol 2:

        sol 3:
            
        """

        for i in range(k):
            last = nums[-1]
            nums.pop()
            nums.insert(0, last)