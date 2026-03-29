class Solution:
    def isPalindrome(self, d):
        newstring = ''
        for z in d:
            if z.isalnum():
                newstring += z.lower()
        return newstring == newstring[::-1]
