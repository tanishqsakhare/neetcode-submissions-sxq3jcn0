class Solution:
    def isPalindrome(self, b):
        newStr = ''
        for f in b:
            if f.isalnum():
                newStr += f.lower()
        return newStr == newStr[::-1]