class Solution:
    def maxProfit(self, prices):
        dynamic_part = {}
        max_profit = 0
        current_min = 100000000000
        for i, price in enumerate(prices):

            profit = price - current_min
            if price < current_min:
                current_min = price
            if profit > max_profit:
                max_profit = profit
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit([1, 3, 5, 8]) == 7
    assert solution.maxProfit([1]) == 0
    assert solution.maxProfit([5, 4, 3, 2, 1]) == 0
