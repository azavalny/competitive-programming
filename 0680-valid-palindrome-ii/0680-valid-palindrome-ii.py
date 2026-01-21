class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        a a a  b  x  c b a a
               l
                     r

        a ... a b
        l       
                r

        z r y x e e d e d e x y z
            l
                              r
        e e d e d e
          l
              r

while l < r:
    if left != right:
        check if either s[l+1:r] or s[l:r-1] are palindromes
    l++
    r--
        """
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        l = 0
        r = len(s) -1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l+1, r) or is_palindrome(l, r-1) # removing one character
            l+=1
            r-=1
        return True