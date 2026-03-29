class Solution:
    def productExceptSelf(self, p):
        n = len(p)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= p[j]
            res[i] = prod
        return res
        