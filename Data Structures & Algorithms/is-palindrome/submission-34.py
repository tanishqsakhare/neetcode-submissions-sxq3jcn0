class Solution:
    def isPalindrome(self, s):
        result = ''
        for r in s:
            if r.isalnum():
                result += r.lower()
        return result == result[::-1]