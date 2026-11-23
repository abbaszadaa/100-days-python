for i in range(1, 11):
    print(i)

for a in range(0, 21, 2):
    print(a)
prices = [95, 100, 105, 110, 90, 120]
for price in prices:
    if price > 100:
        print("BUY Signal")
    elif price < 100:
        print("BELOW THRESHOLD")
    else:
        print("HOLD")
b=10
while b>0:
    print(b)
    b-=1
start_price=50
while start_price<100:
    print("Current Price:", start_price)
    start_price+=10

balance=1000
trade_cost=200
while balance>200:
    print("Current Balance:", balance)
    balance-=trade_cost
for c in range(1,10):
    if c==7:
        break
    print(c)
for d in range(1,10):
    if d==5:
        continue
    print(d)

for e in range(1,4):
    for f in range(1,11):
        print(e*f)

stocks = {
    "Apple": [180, 185, 175],
    "Microsoft": [400, 410, 390],
    "Google": [150, 155, 160]
}
for stock, prices in stocks.items():
    print("Stock:", stock)
    for price in prices:
        print("Price:", price)
stocks1 = {
    "Apple": [180, 185, 175, 190],
    "Microsoft": [400, 410, 390, 420],
    "Google": [150, 155, 145, 160]
}
for stock1, prices1 in stocks1.items():
    print("Stock:", stock1)
    total_count = len(prices1)
    print("Total Count of Prices for", stock1, ":", total_count)
    
    for price1 in prices1:
        print("Price:", price1)
        
        if price1 > 180:
            print("Price is above 180")
        
    average = sum(prices1) / len(prices1)
    print("Average Price for", stock1, ":", average)
