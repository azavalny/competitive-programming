class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        dominant = highest frequency element has count at least half of subarray length (if length > 1)

        find smallest index to split array into 2 with same dominant element

            [1,2,2,      2]
            {1:1, 2:2}   ^   {2: 1}

subarray len  3 
            2 > 3//2            1 > 1
                    2 == 2
                    return right point of 1st subarray
        

        go through each element then update frequency counts of halves to see if you reach dominant element

        [2,1,3,1,1,         1,7,1,2,1]
                 ^          
        {2:1, 1:3, 3:1}     {1:3, 7:1, 2:1}
        3 > 5//2                3 > 5//2
                    1 == 1 
        

        start off with
        {1:1} {2:3}

        left, right half counters dict
        length of left, right half subarrays
        left maximum and check in right

        after each element add from right to left 
        
        {2:2, 1:6, 7:1, 3:1}
        [2,1,3,1,1,1,7,1,2,1]
               i
        {2:1}
        is total count_x - current dominant count_x > (len(nums)-i )//2
index 0 value 1
olddominant 1
Left map Counter({1: 1})
New dominant 1
Check for solution
right half length//2 1
Dominant num total counts 2
Left map dominant counts 1
finished
index 1 value 2
olddominant 1
Left map Counter({1: 1, 2: 1})
New dominant 1
Check for solution
right half length//2 0
Dominant num total counts 2
Left map dominant counts 1
        """
        if len(nums) < 2:
            return -1
        total_counts = Counter(nums)
        left_map = Counter({})
        dominant_num = None
        max_freq_element = 0

        for i in range(len(nums)):
            # print("index", i, "value", nums[i])
            left_map[nums[i]] +=1
            # print("olddominant", dominant_num)
            # print("Left map", left_map)
            if left_map[nums[i]] > left_map[dominant_num]:
                max_freq_element = nums[i]
            # print("New dominant",dominant_num)
            # print("Check for solution")
            # print("right half length//2", (len(nums) - (i+1))//2)
            # print("Dominant num total counts", total_counts[dominant_num])
            # print("Left map dominant counts", left_map[dominant_num])
            if left_map[max_freq_element] > (i+1)//2:
                if total_counts[max_freq_element] - left_map[max_freq_element] > (len(nums) - (i+1))//2:
                    return i
            # print("finished")
        return -1