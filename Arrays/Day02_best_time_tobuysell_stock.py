"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/



-----------------------------------------------------

Approach (Greedy + Single Pass):

1. Track the minimum price seen so far (best day to buy).
2. For each price:
      calculate potential profit = current price - min_price
3. Update maximum profit if current profit is higher.
4. Continue scanning the array once.

-----------------------------------------------------

Time Complexity: O(n)
    → traverse the list once

Space Complexity: O(1)
    → no extra memory used


"""
def max_Profit(prices):
        min_price=float("inf")
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            max_profit=max(max_profit,price-min_price)
        return max_profit    
print(max_Profit([7,1,5,3,6,4]))