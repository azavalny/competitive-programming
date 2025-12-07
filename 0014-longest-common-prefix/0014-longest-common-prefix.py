class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = ""
        for i in range(len(strs[0])):
            currentChar = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != currentChar:
                    return sol
            sol += currentChar
        return sol