class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr_sorted = sorted(arr)
        min_diff = float("inf")
        for i in range(len(arr)-1):
            min_diff = min(min_diff, abs(arr_sorted[i] - arr_sorted[i+1]))
        sol =[]
        for i in range(len(arr)-1):
            if abs(arr_sorted[i] - arr_sorted[i+1]) == min_diff:
                sol.append([arr_sorted[i], arr_sorted[i+1]])
        return sol