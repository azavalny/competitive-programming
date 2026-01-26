class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        [1,2,2,3,5,6] [2,5,6]
         l 
                      r
         p
        l = location before 1st 0 in nums1
        r = end of nums2
        endpointer = end of nums1

        [0]  [1]
        l=0
        r=0
        p=0


        while endpointer > 0:
            if nums1[l] < nums2[r]:
                nums1[endpointer] = nums2[r]
                r--;
                endpointer--;
            if nums1[l] >= nums2[r]:
                nums1[endpointer] = nums1[l]
                l--;
                endpointer--;

        If l < 0, take from nums2
        Else if r < 0, you’re done

        Else compare and place the larger


        """
        l = m-1
        r = len(nums2)-1 # n
        p = len(nums1)-1 # m + n -1
        
        while r >= 0:
            if l < 0 or nums1[l] < nums2[r]: # take from nums2 when nums1 is exhausted or nums2 is larger
                nums1[p] = nums2[r]
                r-=1
            else:
                nums1[p] = nums1[l]
                l-=1
            p-=1

        