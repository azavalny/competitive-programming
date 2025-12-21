class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        
        # row check
        for r in range(len(board)):
            rowVals = Counter(board[r])
            duplicates = [i for i, count in rowVals.items() if count > 1 and i != "."]
            if len(duplicates) > 0:
                return False
        # col check
        for col in zip(*board):
            colVals = Counter(col)
            duplicates = [i for i, count in colVals.items() if count > 1 and i != "."]
            if len(duplicates) > 0:
                return False
        # 3x3 sliding filter check
        rows = len(board)
        cols = len(board[0])
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                square = [board[x + dx][y + dy] for dx in range(3) for dy in range(3)]
                squareVals = Counter(square)
                duplicates = [i for i, count in squareVals.items() if count > 1 and i != "."]
                if len(duplicates) > 0:
                    return False
        return True
