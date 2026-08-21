class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        queue (indexes): [0]

        [2,3,1,1,4]

        q: [  4, 1, 4]

        until queue empty: O(n)
            pop to get right pointer
            loop from min index max index we can reach and add to queue

            stop queue when we reach len(nums)-1

        queue deque([0]) processed 0
r 0
queue deque([1, 2, 3, 4, 5, 6, 7, 8]) processed 8
r 1
queue deque([2, 3, 4, 5, 6, 7, 8]) processed 3
r 2
queue deque([3, 4, 5, 6, 7, 8, 4, 5, 6]) processed 6
r 3
queue deque([4, 5, 6, 7, 8, 4, 5, 6, 7]) processed 7
r 4
queue deque([5, 6, 7, 8, 4, 5, 6, 7, 8]) processed 8
r 5
queue deque([6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) processed 14
r 6
queue deque([7, 8, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) processed 11
r 7
queue deque([8, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) processed 9
r 8
queue deque([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13]) processed 13
r 4
queue deque([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13]) processed 8
r 5
queue deque([6, 7, 8, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14]) processed 14
r 6
queue deque([7, 8, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14]) processed 11
r 7
queue deque([8, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14]) processed 9
r 8
queue deque([9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13]) processed 13
r 9
queue deque([10, 11, 12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 15, 16, 17]) processed 17
r 10
queue deque([11, 12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 15, 16, 17, 18]) processed 18
r 11
queue deque([12, 13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 15, 16, 17, 18]) processed 11
r 12
queue deque([13, 14, 10, 11, 12, 13, 9, 10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 15, 16, 17, 18, 12, 13, 14, 15, 16, 17, 18, 19, 20]) processed 20
        """
        queue = deque([0])
        processed = 0

        while queue:
            #print("queue", queue, "processed", processed)
            r = queue.popleft()
            #print("r", r)
            if r == len(nums)-1:
                return True
            for i in range(processed+1, r + nums[r]+1):
                if i > processed:
                    queue.append(i)
            processed = max(processed, r + nums[r])
        return False