class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        next greater = first greater to the right of x
        nums1 subset of nums2

        for each number in nums1 find its corresponding number in nums2 and determine the next greater element of that corresponding number in nums2

        return ans[i] next greater element after corresponding nums2 number from nums1

        all integers unique

        O(n^2)
        loop over every num in nums1: 
            find equal element in nums2 O(1) with precomputed hashmap
            use decreasing monotonic stack to find next greater element after equal nums2 element O(n)
        
        nums1 = [4,1,2], nums2 = [1,3,4,2]
                   i
                                    j


        preprocess nums2 once with monotonic decreasing stack to compute next greater element for every value in nums2
        """
        stack = []
        next_greater = {}

        # build monotonically decreasing stack of values from nums2
        for n in nums2:
            while stack and n > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = n
            stack.append(n)
        # anything left in stack has no next greater
        for n in stack:
            next_greater[n] = -1
        
        return [next_greater[x] for x in nums1]