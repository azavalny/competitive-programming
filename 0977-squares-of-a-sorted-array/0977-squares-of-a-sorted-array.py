class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = [n for n in nums if n*-1 > 0]
        pos = [n for n in nums if n*1 > 0]
        zeros = [n for n in nums if n == 0]
        sol = zeros

        l = len(neg)-1
        r = 0
        while l >= 0 and r < len(pos):
            if neg[l]**2 == pos[r]**2:
                sol.append(neg[l]**2)
                sol.append(pos[r]**2)
                r +=1
                l -= 1
            elif neg[l]**2 > pos[r]**2:
                sol.append(pos[r]**2)
                r +=1
            else:
                sol.append(neg[l]**2)
                l -=1
        while l >= 0:
            sol.append(neg[l]**2)
            l -=1
        while r < len(pos):
            sol.append(pos[r]**2)
            r +=1
        return sol
