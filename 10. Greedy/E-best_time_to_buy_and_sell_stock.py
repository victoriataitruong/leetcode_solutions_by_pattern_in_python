"""
Leetcode 121: Best Time to Buy and Sell Stock

Problem Description:
You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i-th` day. 
You want to maximize your profit by choosing a single day to buy one stock and choosing a later day to sell that stock.
Return the maximum profit you can achieve from this transaction. If no profit can be made, return `0`.
The solution must be solved in **O(n)** time complexity, where `n` is the number of days.

Problem Type: Greedy

Approach:
1. **Track the Minimum Price**: Keep track of the lowest price encountered so far as you iterate through the list of prices.
2. **Calculate Potential Profit**: For each price, calculate the potential profit by subtracting the minimum price from the current price.
3. **Track Maximum Profit**: Keep track of the maximum profit by comparing the current profit with the previously recorded maximum profit.
4. **Return the Maximum Profit**: After iterating through the list, return the maximum profit found. If no profit is possible, return 0.

Example: [7, 1, 5, 3, 6, 4]
Initially             min_price = Infinity       max_profit = 0
price[i] = 7         min_price = 7             max_profit = 0
price[i] = 1         min_price = 1             max_profit = 0
price[i] = 5         min_price = 1             max_profit = 4
price[i] = 3         min_price = 1             max_profit = 4
price[i] = 6         min_price = 1             max_profit = 5
price[i] = 4         min_price = 1             max_profit = 5

Return 5

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
profit = maxProfit(prices)
print(f"Maximum profit: {profit}")
