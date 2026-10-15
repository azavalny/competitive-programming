class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        p pairs of indicies to min max absolute difference among all pairs
            no duplicates
        max of empty set is 0

        brute force, compute all pairs distances, add to min heap, and pop p pairs without repeating

        [10,1,2,7,1,3], p=2

        1-1, 2-3 = max(0, 1)=1

        [4,2,1,2]

        2-2 = 0


        sort values and do binary search over differences (0, max - min from nums[-1]-nums[0])

        [1, 3, 3, 4], p=2

        0 1 2 3 4       range of difference answers
        l
          m
            r
        
        m=2, try 1-3=2, 3-4=1 
            p=0, found solution but try to reduce even further
        m=1, 1-3, 3-3=0, 4 
            p=1, not found solution
        
        check how many pairs we formed such that at end of loop we have p=0 and keep retrying binary search

l 0
r 3
mid 1
i 0
diff 1
pairs_formed 1
##################
i 2
diff 2
pairs_formed 1
##################
total pairs_formed 1
Valid 1
Sol updated 1
        """
        def is_valid(target):
            pairs_formed = 0
            i=0
            while i < len(nums)-1:
                # print("i", i)
                # print("diff", abs(nums[i] - nums[i+1]))
                if abs(nums[i] - nums[i+1]) <= target:
                    pairs_formed+=1
                    i+=2
                else:
                    i+=1
            #     print("pairs_formed", pairs_formed)
            #     print("##################")
            # print("total pairs_formed", pairs_formed)
            return pairs_formed >= p

        nums.sort()
        max_diff = nums[len(nums)-1]-nums[0]
        l=0
        r=max_diff
        sol = max_diff

        while l <= r:
            mid = (l + r)//2
            # print("l",l)
            # print("r", r)
            # print("mid", mid)

            if is_valid(mid):
                # print("Valid", mid)
                sol = min(sol, mid)
                r = mid -1
                # print("Sol updated", sol)
            else:
                l = mid + 1
        return sol