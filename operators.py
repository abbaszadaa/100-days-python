a=25
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
stock_price=90
is_profitable = True
buyed_signal=stock_price<100 and is_profitable
print( buyed_signal)
name=input('Enter your name:')
age=int(input('Enter your age:'))
print("Name:", name)
print("Age after 5 years:", age+5)
current_price=int(input('Enter current stock price:'))
buy_price=int(input('Enter buy price:'))
share_count=int(input('Enter number of shares:'))
print("Profit:", (current_price-buy_price)*share_count)
print("Profit percentage:", (current_price-buy_price)/buy_price*100)