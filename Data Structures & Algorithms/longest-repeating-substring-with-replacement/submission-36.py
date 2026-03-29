class Solution:
    def characterReplacement(self, p, q):
        res = 0
        for t in range(len(p)):
            count, maxf = {}, 0
            for u in range(t, len(p)):
                count[p[u]] = 1 + count.get(p[u], 0)
                maxf = max(maxf, count[p[u]])
                if (u - t + 1) - maxf <= q:
                    res = max(res, u - t + 1)
        return res