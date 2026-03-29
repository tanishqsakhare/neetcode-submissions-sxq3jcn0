class Solution:
    def isPalindrome(self, s):
        result = ''
        for p in s:
            if p.isalnum():
                result += p.lower()
        return result == result[::-1]