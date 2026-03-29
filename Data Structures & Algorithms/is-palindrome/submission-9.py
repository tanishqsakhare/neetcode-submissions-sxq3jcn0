class Solution:
    def isPalindrome(self, s: str):
        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]