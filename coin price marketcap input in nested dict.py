coins = {}
for x in range(3):
    coin = str(input("enter name of coin : "))
    coin_price = float(input("enter coin price : "))
    coin_marketcap = int(input("enter coin market cap : "))
    coin_metrix = {coin_price:coin_marketcap}
    coins[coin] = coin_metrix
print(coins)