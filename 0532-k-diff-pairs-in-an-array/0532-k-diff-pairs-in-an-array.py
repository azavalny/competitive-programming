class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        find unique pairs where abs(difference between first and second) equals k and first is before second
            can be negative
        [3,1,4,1,5] k =2

        sort nums
        
        check if nums[i]-k is in the hashset of values we've visited
            don't increment solution if we've seen the value before
            otherwise add value to set

        nums[j] - nums[i] == k
        nums[i] = nums[j] - k
        
        [1,2,3,4,5] k =1
                 i
    set(1,2, 3, 4, 5)
    sol = 1+1+1+1


        [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1]
    = [1, 1, 1, 1,  1, 1, 1, 1, 2, 2, 2, 2]
                                i
        """
        nums.sort()
        visited = set()
        sol = 0
        i=0
        while i < len(nums):
            n = nums[i]
            if k == 0 and n in visited:
                sol+=1
                last = n
                while i < len(nums) and nums[i] == last:
                    print(i)
                    i+=1
                continue
            if n not in visited and n-k in visited:
                sol +=1
            visited.add(n) # set property
            i+=1
        return sol