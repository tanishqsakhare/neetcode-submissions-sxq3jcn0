class Solution:
    def isPalindrome(self, p):
        strng = ''
        for x in p:
            if x.isalnum():
                strng += x.lower()
        return strng == strng[::-1]