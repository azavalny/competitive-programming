class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from collections import deque
        """
        array sorted solution sorted
        [1, 2, 3, 4, 5] k = 4, x = 3
         L 
                     R
lhalf=[1, 2] <-- prepend 
rhalf=[4] <-- append
return lhalf + [3] + rhalf
         [1, 1, 2, 3, 4, 5] k=4, x = -1
          L
                   R
         [1, 1, 2, 3, 4, 5] k=4, x = 20
                L
                         R
        1. find closest element in array to x using binary search to anchor center of window
        2. left and right pointers expand until they are k distance away from each other
            if k is at least 2:
                add both arr[L] and arr[R]
            otherwise
                pick closer number between arr[L] and arr[R] and choose smaller to break tie
            move BOTH L and R away from center
                If one pointer goes out of bounds keep expanding valid side
        """
        # find closest element to x using binary search
        def find_center(nums, x):
            r = len(nums)-1
            l = 0
            while l <= r:
                mid = l + (r-l) //2
                if nums[mid] == x:
                    return mid
                elif nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid -1
            return l

        r = find_center(arr, x)
        l = r -1
        sol = deque()

        while k > 0:
            if l < 0:
                sol.append(arr[r])
                r +=1
            elif r >= len(arr):
                sol.appendleft(arr[l])
                l-=1
            else:
                # pick closer
                if x - arr[l] <= arr[r] - x:
                    sol.appendleft(arr[l])
                    l-=1
                else:
                    sol.append(arr[r])
                    r +=1
            k -=1
        return list(sol)