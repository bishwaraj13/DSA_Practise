# https://leetcode.com/problems/online-stock-span/description/
class StockSpanner:

    def __init__(self):
        self.stock_prices = []
        self.stock_index = -1
        self.stack = []
        
    def next(self, price: int) -> int:
        self.stock_prices.append(price)
        self.stock_index += 1

        while self.stack and self.stock_prices[self.stack[-1]] <= price:
            self.stack.pop()

        if self.stack:
            prev_greatest_index = self.stack[-1]
            result = self.stock_index - prev_greatest_index
        else:
            result = self.stock_index + 1  # If stack empty, span is all days so far

        self.stack.append(self.stock_index)

        return result