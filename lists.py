apple=[100, 105, 110, 95, 120]
print("Apple prices:", apple)
print(apple[0]) 
print(apple[2]) 
print(apple[4])
apple[1]=115
print("Updated Apple prices:", apple[1])
print(len(apple))
print("First price:", apple[0])
print("Last price:", apple[-1])
print("Price changes:", apple[4]-apple[0])

banana = [150, 155, 148, 160]
banana.append(165)
banana.insert(2, 152)
print("Banana prices:", banana)
print(len(banana))
stock_prices = [200, 210, 195, 220, 230]
stock_prices.remove(195)
stock_prices.pop(2)
print("Stock prices:", stock_prices)
stock_prices1 = [180, 120, 200, 150, 170]
stock_prices1.sort()
print("Sorted stock prices:", stock_prices1)
stock_prices1.sort(reverse=True)
print("Sorted stock prices in descending order:", stock_prices1)
stock_prices2 = [180, 120, 200, 150, 170]
stock_prices2.reverse()
print("Reversed stock prices:", stock_prices2)
