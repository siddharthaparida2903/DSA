class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## TWO POINTER
        l, r = 0, 1 # buy, sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP
            

        
        ## BRUTEFORCE
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         res = max(res, sell - buy)
        # return res