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
    assert 5 == solution.maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == solution.maxProfit([6, 5, 4, 3, 2, 1])
