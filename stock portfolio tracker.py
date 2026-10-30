
def stock_portfolio_tracker():
    print("===== STOCK PORTFOLIO TRACKER =====")

    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 410,
        "AMZN": 175
    }

    total_investment = 0

    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(stock, ":", "$", price)

    while True:
        stock_name = input(
            "\nEnter stock symbol (or DONE to finish): "
        ).upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Invalid stock symbol!")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Please enter a valid quantity.")
            continue

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock:", stock_name)
        print("Investment Value: $", investment)

    print("\n===== PORTFOLIO SUMMARY =====")
    print("Total Investment: $", total_investment)
    print("Thank you for using Stock Portfolio Tracker!")


stock_portfolio_tracker()
