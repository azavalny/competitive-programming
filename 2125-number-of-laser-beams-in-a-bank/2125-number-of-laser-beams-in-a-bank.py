class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        one beam between two security devices if:
            devices on different rows
            at least 1 blank row between them
        undirected lasers

        011001 = 3
        000000
        010100 = 2
        001000 = 1
        3*2 + 2*1 = 8

        number of devices in first row * devices in third row

        011001
        000000
        000000
        001000

        prevValidRowSum
        for each row:
            if row is all 0's we skip
            otherwise multiply current row by prevValidRowSum and increment solution
            update prevValidRowSum
        """
        bank = [[int(c) for c in r] for r in bank]
        prevValidRowSum = 0
        sol = 0
        for row in bank:
            if sum(row) == 0:
                continue
            sol += sum(row)*prevValidRowSum
            prevValidRowSum = sum(row)
        return sol