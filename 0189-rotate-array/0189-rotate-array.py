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

        for i in range(k): #O(nk) ~= O(n^2)
            last = nums[-1]
            nums.pop()
            nums.insert(0, last) #O(n)

        sol 2: O(n)
            reverse nums
            reverse first k elements
            reverse the rest of the k elements

            [7,6,5,4,3,2,1] k = 3
            [5, 6, 7,4,3,2,1] reverse 1st k
            [5, 6, 7, 1, 2, 3, 4] reverse nums[k:]


        sol 3:
            
        """
        k%=len(nums)
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        rev(0, len(nums)-1)
        rev(0, k-1)
        rev(k, len(nums)-1)