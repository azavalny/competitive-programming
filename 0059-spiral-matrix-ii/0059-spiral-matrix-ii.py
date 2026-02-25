class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        nxn matrix in spiral order

        run spiral matrix algorithm while incrementing i
        """
        ROWS, COLS = n, n

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        left, right, top, bottom = 0, ROWS-1, 0, COLS-1

        count=1

        while left <= right and top <= bottom:
            for col in range(left, right+1):
                matrix[top][col] = count
                count+=1
            top+=1

            for row in range(top, bottom+1):
                matrix[row][right] = count
                count +=1
            right -=1

            if left <= right:
                for col in range(right, left-1, -1):
                    matrix[bottom][col] = count
                    count+=1
                bottom-=1
            
            if top <= bottom:
                for row in range(bottom, top-1, -1):
                    matrix[row][left] = count
                    count+=1
                left+=1
        return matrix

