class Solution:
    def isPalindrome(self, s):
        string = ''
        for p in s:
            if p.isalnum():
                string += p.lower()
        return string == string[::-1]