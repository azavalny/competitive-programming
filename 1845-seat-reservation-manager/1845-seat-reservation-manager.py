class SeatManager:
    """
    state of n seats 1 to n
    all initially available

    reserve --> reserves smallest number unreserved seat and returns its number
    unreserve --> unreserves seat i

    store in list/min heap

    O(n^2)
boolean array (index to seat):
+ pointer to leftmost smallest numbered unreserved seat (move back and forth for calls to reserve() and unreserve())
    [1, 1, 0, 0, 0],n=5
           n
    reserve() -->1, [1, 0, 0, 0, 0], n=2
    reserve()-->2   [1, 1, 0, 0, 0], n=3
    unreserve(2)    [1, 0, 0, 0, 0], n=2 (while)
    reserve()-->2   [1, 1, 0, 0, 0], n=3
    reserve()-->3 [1, 1, 1, 0, 0], n=4
    reserve()-->4 [1, 1, 1, 1, 0], n=5
    reserve()-->5 [1, 1, 1, 1, 1], n=6
    unreserve(5) [1, 1, 1, 1, 0], n=5


    efficient:
        use min heap for available seats
            pop them on reserve
            insert on unreserve()
    """

    def __init__(self, n: int):
        self.available = [i for i in range(1, n+1)]
    """
    it is guaranteed that there will be at least one unreserved seat.
    """
    def reserve(self) -> int:
        return heapq.heappop(self.available)

    """
    it is guaranteed that seatNumber will be reserved
    """ 
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)