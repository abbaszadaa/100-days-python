digit=float(input("Enter a digit: "))
if digit>0:
    print("The digit is positive.")
elif digit==0:
    print("The digit is zero.")
else:
    print("The digit is negative.")
price=float(input("Enter the stock price: "))
if price<100:
    print("Buy")
elif price==100:
    print("Hold")
else:
    print("Sell")
profit=float(input("Enter profit: "))
if profit>0:
    print("Profit")
elif profit==0:
    print("BREAK EVEN")
else:
    print("Loss")

stock_price=float(input("Enter stock price: "))
is_profitable=input("Is it profitable? (Yes/No): ")
if stock_price>100 and  is_profitable=="No":
    print("Sell")
elif stock_price>100 and is_profitable=="Yes":
    print("Hold")
elif stock_price<100 and is_profitable=="Yes":
    print("Wait")
else:
    print("Sell")

risk_score = int(input("Enter your risk score (0-100): "))

if risk_score < 0 or risk_score > 100:
    print("Invalid risk score.")
elif risk_score <= 30:
    print("Low")
elif risk_score <= 60:
    print("Medium")
else:
    print("High")



          