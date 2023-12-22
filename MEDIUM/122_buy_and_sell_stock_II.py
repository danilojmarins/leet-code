class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        i = 0
        j = 1
        max_value = 0

        while j < len(prices):
            if prices[j] > prices[i]:                                   # if next > prev
                max_value = prices[j]                                   # save max so far
                while j < len(prices) and prices[j] >= max_value:       # repeat until after local max
                    max_value = prices[j]
                    j += 1
                max_profit += prices[j-1] - prices[i]                   # profit = local max - prices[i]
                i = j - 1
            else:                                                       # if next <= prev
                i += 1                                                  # move both pointers
                j += 1

        return max_profit
    
## Time Complexity = O(n)