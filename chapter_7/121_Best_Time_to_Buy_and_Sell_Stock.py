'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



한번의 거래로 낼 수 있는 최대 이익 산출

예시

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

'''

def maxProfit(prices):
    max_price = 0

    for i , price in enumerate(prices):
        for j in range(i,len(prices)):
            max_price = max(prices[j] - price,max_price)

    return max_price

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

