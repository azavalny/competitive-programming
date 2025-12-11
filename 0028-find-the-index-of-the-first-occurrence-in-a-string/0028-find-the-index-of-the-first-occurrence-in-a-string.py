class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                window = 0
                for j in range(len(needle)):
                    if i + j < len(haystack) and haystack[i + j] == needle[j]:
                        window +=1
                if window == len(needle):
                    return i
        return -1