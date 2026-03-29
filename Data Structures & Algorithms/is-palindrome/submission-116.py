class Solution:
    def isPalindrome(self, s):
        newstring = ''
        for c in s:
            if c.isalnum():
                newstring += c.lower()
        return newstring == newstring[::-1]