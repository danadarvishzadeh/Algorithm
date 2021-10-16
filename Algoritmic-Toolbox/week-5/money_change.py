def change(money, coins):
    min_num_coins = [0]
    for i in range(1, money+1):
        min_num_coins.append(1000)
        for coin in coins:
            if coin <= i:
                min_num_coins[i] = min(min_num_coins[i], min_num_coins[i-coin] + 1)
    return min_num_coins[money]

money = int(input())
coins = [1, 3, 4]
print(change(money, coins))
