class Solution:
    def isPalindrome(self, s):
        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]
