class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        _min = prices[0]            # min value so far
        max_profit = 0              # max profit so far

        for i in range(len(prices)):
            if prices[i] - _min > max_profit:   # if current - min > profit, update profit
                max_profit = prices[i] - _min
            if prices[i] < _min:                # if current < min, update min
                _min = prices[i]                # min is always updated after profit
        
        return max_profit
    
## Time Complexity = O(n) -> Beats 99.93%