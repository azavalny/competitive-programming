class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        First integer of each row is greater than last integer of previous row

        apply binary search where for finding middle we can convert the midpoint to coordinates mapping

            row = index // n
            col = index % n

            Every n indices → move to the next row (row)
            remainder is position in the row (column)

        for left and right pointers we have to check for boundary conditions by restarting on next row/previous row
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n -1

        while l <= r:
            mid = l + (r-l)//2
            row, col = mid //n, mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid -1
        return False