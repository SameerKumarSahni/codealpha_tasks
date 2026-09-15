# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:

    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print(f"{stock} added successfully.")
    print(f"Investment value: ${investment}")


print("\n===== PORTFOLIO SUMMARY =====")

for item in portfolio:
    print(
        f"{item['stock']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ${item['price']} | "
        f"Value: ${item['investment']}"
    )

print("------------------------------")
print(f"Total Investment: ${total_investment}")
