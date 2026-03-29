class Solution:
    def isPalindrome(self, t):
        string = ''
        for d in t:
            if d.isalnum():
                string += d.lower()
        return string == string[::-1]