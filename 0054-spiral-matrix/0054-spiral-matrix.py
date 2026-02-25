class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        define 4 grid lines (top, bottom left, right) and shrink them inwards
        define directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) and cycle through them dir = (dir + 1)%4
mxn
top = 0
bottom = m-1
left=0
right = n-1

while top <= bottom and left <= right:
    go left--> right across
    move top down

    go top--> bottom on right
    right goes left

    go right--> left across bottom
    bottom goes up

    go bottom--> top on left
    left goes right
    
       L  R
       |  |
    [1,|2,|3]
__________________ T
    [4,|5,|6]
__________________ B
    [7,|8,|9]
       |  |

    R
    L
[1, 2, 3,4]
[5, 6, 7,8]  B
[9,10,11,12] T

sol = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

 L
R
[7] 
[9] T B
[6] 

[7, 9, 6]

        """
        ROWS, COLS = len(matrix), len(matrix[0])
        top = 0
        bottom = ROWS-1
        left=0
        right = COLS-1

        sol = []
        while top <= bottom and left <= right:
            for col in range(left, right+1):
                sol.append(matrix[top][col])
            top+=1

            for row in range(top, bottom+1):
                sol.append(matrix[row][right])
            right-=1
            
            if top <= bottom:
                for col in range(right, left-1, -1):
                    sol.append(matrix[bottom][col])
                bottom-=1

            if left <= right:
                for row in range(bottom, top-1, -1):
                    sol.append(matrix[row][left])
                left+=1

        return sol