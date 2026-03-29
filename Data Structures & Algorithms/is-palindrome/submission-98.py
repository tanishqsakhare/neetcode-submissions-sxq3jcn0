class Solution:
    def isPalindrome(self, s):
        string = ''
        for c in s:
            if c.isalnum():
                string += c.lower()
        return string == string[::-1]

