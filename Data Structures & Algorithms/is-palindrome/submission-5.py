class Solution:
    def isPalindrome(self, s: str):
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
        return res == res[::-1]