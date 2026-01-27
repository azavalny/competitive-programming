class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        return # unique elements while removing duplicates after first appearance
        nums is sorted so consecutive elements must be increasing

        [1 ,2, 2]
            l
               r


        return k=2
        [1, 2, _]

        [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
                     l
                                    r
        l = start
        r = 2nd unique element
        while r < len(nums):
            2nd element overwritten with R
            L+=1
            move R until it finds new element if R not at end
        return L+1
        return k=5
        [0, 1, 2, 3, 4, _, _, _, _, _]

        [1, 1]
         l
            r

        """

        l = 0
        r = 0
        startElement = nums[0]
        for i in range(len(nums)):
            if nums[i] != startElement:
                r = i
                break
        if r == 0:
            nums = [startElement]
            return 1

        while r < len(nums):
            if l + 1 < len(nums):
                nums[l + 1] = nums[r]
            l+=1
            curElement = nums[r]
            while r < len(nums) and curElement == nums[r]:
                r+=1
        return l+1
            