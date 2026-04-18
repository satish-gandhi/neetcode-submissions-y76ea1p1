class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        l=0
        r=1
        while r<len(prices):
            P = prices[r]-prices[l]
            maxP = max(maxP, P)
            if prices[r]<prices[l]:
                l+=1
            else:
                r+=1
        return maxP