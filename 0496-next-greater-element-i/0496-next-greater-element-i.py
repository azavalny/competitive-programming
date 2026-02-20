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
        """
        sol = []

        nums2map = {v: i for i, v in enumerate(nums2)} # we can do this because input nums unique
        stack = []
        for n1 in nums1:
            nextIndex = nums2map[n1]
            solFound = False
            for j, n2 in enumerate(nums2[nextIndex:]):
                if stack and n2 > n1:
                    sol.append(n2)
                    solFound = True
                    break
                else:
                    stack.append(n2)
            if not solFound:
                sol.append(-1)
            stack = []
        return sol