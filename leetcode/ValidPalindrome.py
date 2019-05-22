class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        b = 0
        e = len(s) - 1
        while b <= e:
            if not (s[b].isalpha() or s[b].isnumeric()):
                b += 1
                continue
            if not (s[e].isalpha() or s[e].isnumeric()):
                e -= 1
                continue
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1
        return True