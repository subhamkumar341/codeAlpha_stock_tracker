import csv

# Step 1: Predefined car prices in ₹
car_prices = {
    "TESLA": 6000000,
    "BMW": 4500000,
    "TATA": 800000,
    "HYUNDAI": 1000000,
    "TOYOTA": 1500000
}

portfolio = {}
total_investment = 0

print("🚗 Welcome to Car Portfolio Tracker!")
print("Available Cars and Prices (in ₹):")
for car, price in car_prices.items():
    print(f"- {car} : ₹{price}")

print("\n📥 Enter your car holdings (type 'done' to finish):")

# Step 2: Get input from user
while True:
    car_name = input("Enter car brand (e.g., TESLA): ").upper()

    if car_name == "DONE":
        break

    if car_name not in car_prices:
        print("⚠️ Car not available. Try again.\n")
        continue

    try:
        qty = int(input(f"Enter quantity of {car_name}: "))
    except ValueError:
        print("⚠️ Invalid number. Try again.\n")
        continue

    portfolio[car_name] = portfolio.get(car_name, 0) + qty
    print(f"✅ Added {qty} unit(s) of {car_name}\n")

# Step 3: Show investment summary
print("\n📊 Your Car Investment Summary:")
csv_rows = [["Car", "Quantity", "Price (₹)", "Value (₹)"]]  # Header row for CSV

for car, qty in portfolio.items():
    price = car_prices[car]
    value = price * qty
    print(f"{car} - {qty} unit(s) @ ₹{price} = ₹{value}")
    total_investment += value
    csv_rows.append([car, qty, price, value])

print(f"\n💰 Total Investment Value: ₹{total_investment}")
csv_rows.append(["", "", "Total", total_investment])

# Step 4: Save to CSV file
filename = "car_portfolio_summary.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_rows)

print(f"\n✅ Summary saved to CSV file: {filename}")
