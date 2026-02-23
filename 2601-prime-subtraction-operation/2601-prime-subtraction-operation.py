class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        """
        pick number and pick prime less than number and subtract prime from number
        can you make nums a strictly increasing array doing the above operations?

        invariant: find smallest possible difference that keeps increasing order using binary search:
            if diff maintains increasing order:
                choose larger prime by moving to right half < nums[i]
            else
                choose smaller prime by moving to left

        subtract nums[i] - biggest prime less than nums[i]

        [4, 9, 6, 8]
                  i
 prime   3  7  5  2
diff     1  2  3  6

primes[0, 10] = 2, 3, 5, 7
                      L
                         R

        [6,8,11,12] sorted in increasing order so no stack violation

        [5, 8,4]
              i
prime    3  5       <== keep current element
diff     2  3 4

maxprime 2, 3, 5, 7
                  L
                  R
        """
        if len(nums) < 2:
            return True
        max_val = max(nums)
        def cal_primes(n):
            is_primes = [True]*n
            is_primes[0] = is_primes[1] = False

            for i in range(2, int(math.sqrt(n))+1):
                if is_primes[i]:
                    for mul in range(i*i, n, i):
                        is_primes[mul] = False
            return is_primes
        
        primes = cal_primes(max_val)
        primes = [i for i in range(len(primes)) if primes[i]]

        sol = []
        for n in nums:
            last_valid_diff = None
            left, right = 0, len(primes)-1
            while left <= right:
                mid = (left + right) //2
                prime = primes[mid]

                if n <= prime:
                    right = mid-1
                    continue

                diff = n - prime
                if len(sol) == 0 or diff > sol[-1]:
                    # right side increasing order no violation
                    left = mid + 1
                    last_valid_diff = diff
                else:
                    # left side increasing order violated
                    right = mid - 1
            
            if last_valid_diff is None:
                if len(sol) == 0 or n > sol[-1]:
                    sol.append(n)
                else:
                    return False
            else:
                sol.append(last_valid_diff)

        return len(sol) == len(nums)