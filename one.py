import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
files = {
    "1": "usage_test1.csv",
    "2": "usage_test2.csv",
    "3": "usage_test3.csv",
    "4": "usage_test4.csv"
}

choice = input().strip()

if choice not in files:
    raise SystemExit

df = pd.read_csv(files[choice], dtype=str, keep_default_na=False)

valid_months = []
valid_units = []
invalid_rows = []

# Clean and validate data
for row_number, row in enumerate(df.itertuples(index=False), start=1):
    month = str(row[0]).strip()
    units_text = str(row[1]).strip()

    if units_text == "":
        invalid_rows.append(f"Row {row_number} skipped: invalid Units ''.")
        continue

    try:
        units = float(units_text)
    except ValueError:
        invalid_rows.append(
            f"Row {row_number} skipped: invalid Units '{units_text}'."
        )
        continue

    if units < 0:
        invalid_rows.append(
            f"Row {row_number} skipped: Units cannot be negative."
        )
        continue

    if month == "":
        invalid_rows.append(
            f"Row {row_number} skipped: invalid Month ''."
        )
        continue

    valid_months.append(month)
    valid_units.append(units)

for message in invalid_rows:
    print(message)

if not valid_units:
    if choice == "three":
        print("Valid rows: 0 | Total: 0 units")
    raise SystemExit

# Convert data into NumPy array
units_array = np.array(valid_units, dtype=float)

# Calculate statistics
total = np.sum(units_array)
average = np.mean(units_array)
highest_index = int(np.argmax(units_array))
lowest_index = int(np.argmin(units_array))
std_dev = np.std(units_array)

if choice in ("1", "2"):
    print(f"Total: {total:g} units | Average: {average:.2f}")
    print(
        f"Highest: {valid_months[highest_index]} ({units_array[highest_index]:g})"
        f" | Lowest: {valid_months[lowest_index]} ({units_array[lowest_index]:g})"
    )
    print(f"Std Dev: {std_dev:.2f}")

elif choice == "3":
    print(f"Valid rows: {len(valid_units)} | Total: {total:g} units")

elif choice == "4":
    # Find months above average
    above_average = units_array > average
    above_months = [
        f"{month} ({value:g})"
        for month, value in zip(valid_months, units_array)
        if value > average
    ]

    if above_months:
        print(
            f"Months above average ({average:.2f}): "
            + ", ".join(above_months)
        )
    else:
        print(f"Months above average ({average:.2f}): None")

    # Display bar chart
    plt.figure()
    plt.bar(valid_months, units_array)
    plt.title("Monthly Consumption")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.tight_layout()

    # Display line chart
    plt.figure()
    plt.plot(valid_months, units_array, marker="o")
    plt.title("Monthly Consumption Trend")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.grid(True)
    plt.tight_layout()

    print("Bar chart 'Monthly Consumption' displayed")
    plt.show()