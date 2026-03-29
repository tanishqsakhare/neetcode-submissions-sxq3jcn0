class Solution:
    def isPalindrome(self, d):
        string = ''
        for t in d:
            if t.isalnum():
                string += t.lower()
        return string == string[::-1]