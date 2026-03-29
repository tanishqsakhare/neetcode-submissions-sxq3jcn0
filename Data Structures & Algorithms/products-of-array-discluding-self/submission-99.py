class Solution:
    def productExceptSelf(self, y):
        res = [0] * len(y)
        for i in range(len(y)):
            prod = 1
            for j in range(len(y)):
                if i == j:
                    continue
                prod *= y[j]
            res[i] = prod
        return res