n = int(input())

coins = [10, 5, 1]
min_coin = 0
for coin in range(len(coins)):
    min_coin += n // coins[coin]
    n = n % coins[coin]

print(min_coin)
