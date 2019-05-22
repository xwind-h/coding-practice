class Solution:
    def maxProfit(self, prices):
        size = len(prices)
        if size < 2:
            return 0
        max_benfit = 0
        for i in range(size):
            for j in range(i+1, size):
                bf = prices[j] - prices[i]
                max_benfit = bf if bf > max_benfit else max_benfit
        return max_benfit

    def maxProfit2(self, prices):
        size = len(prices)
        if size <= 1:
            return 0
        max_sofar = 0
        max_ending = 0
        for i in range(1, size):
            tmp = max_ending + prices[i] - prices[i-1]
            max_ending = tmp if tmp > 0 else 0
            max_sofar = max_ending if max_ending > max_sofar else max_sofar
        return max_sofar
            
    