class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        naive O(n^2): for each element
                    find greatest to right
        O(n)
        [17, 18, 5, 4, 6, 1]
maxSeen  18  18  6  6  6  1
from left
        """
        newArr = [0]*len(arr)
        curMax = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            newArr[i] = curMax
            curMax = max(curMax, arr[i])
        newArr[-1] = -1
        return newArr