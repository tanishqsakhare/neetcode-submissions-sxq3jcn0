class Solution:
    def productExceptSelf(self, u):
        res = [0] * len(u)
        for i in range(len(u)):
            prod = 1
            for j in range(len(u)):
                if i == j:
                    continue
                prod *= u[j]
            res[i] = prod
        return res