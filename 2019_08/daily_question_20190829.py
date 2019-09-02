'''
You are given an array. Each element represents the price of a stock on that particular day.
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
'''

def buy_and_sell(arr):
    min = arr[0]
    max = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        if (arr[i] < min):
            min = arr[i]
            max = arr[i]
        if (arr[i] > max):
            max = arr[i]
        if (max-min > max_diff):
            max_diff = max-min    

    return max_diff

print (buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
