class Solution:
    def isPalindrome(self, s):
        res = ''
        for y in s:
            if y.isalnum():
                res += y.lower()
        return res == res[::-1]