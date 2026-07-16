class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        n = len(prices)
        res = 0
        l = 0
        r = 1
        while r<n:
            if prices[r]<=prices[l]:
                l = r 
                r += 1
            else:
                res = max(res, prices[r]- prices[l])
                r+=1
        return res


# 10 1 5 3 5 7 1 
