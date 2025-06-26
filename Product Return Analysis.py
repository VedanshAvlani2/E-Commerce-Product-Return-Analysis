import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# Load and Preprocess Data
# --------------------------
df = pd.read_csv("order_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Month'] = df['Date'].dt.to_period('M')

# Interpret -1 as return
df['Returned'] = df['Refunded Item Count'] == -1

# --------------------------
# KPI Calculations
# --------------------------
total_orders = len(df)
total_returns = df['Returned'].sum()
return_rate = round((total_returns / total_orders) * 100, 2)

print("📦 E-COMMERCE RETURNS ANALYSIS")
print("-" * 40)
print(f"Total Orders         : {total_orders:,}")
print(f"Total Returned Items : {total_returns:,}")
print(f"Return Rate          : {return_rate}%")

# Monthly return rate
monthly_return_rate = df.groupby('Month')['Returned'].mean().round(3)
print("\n📅 Monthly Return Rates:")
print(monthly_return_rate.to_string())

# Top returned items
top_returned = df[df['Returned']]['Item Name'].value_counts().head(10)
print("\n🔝 Top 10 Returned Items:")
print(top_returned.to_string())

# Return rate per buyer
buyer_return_rate = df.groupby('Buyer ID')['Returned'].mean().round(3)
print(f"\n👤 Customers with > 50% return rate: {(buyer_return_rate > 0.5).sum()}")
print(f"👤 Customers with no returns       : {(buyer_return_rate == 0).sum()}")
print(f"👤 Average Return Rate per Buyer   : {buyer_return_rate.mean():.2%}")

# Return Rate Over Time
monthly_returns = df[df['Refunded Item Count'] == -1].resample('M', on='Date').size()
print(f"📅 Months Covered: {monthly_returns.index.min().strftime('%b %Y')} to {monthly_returns.index.max().strftime('%b %Y')}")
print(f"📈 Average Monthly Returns: {monthly_returns.mean():.2f}")

# Return Rate by Product Category
category_return_rate = df.groupby('Category')['Refunded Item Count'].apply(lambda x: (x == -1).mean() * 100).sort_values(ascending=False)
print("📦 Return Rate by Product Category (%):")
print(category_return_rate.round(2).to_string())

# Return Rate vs. Quantity Ordered
returned_qty_avg = df[df['Refunded Item Count'] == -1]['Final Quantity'].mean()
non_returned_qty_avg = df[df['Refunded Item Count'] == 0]['Final Quantity'].mean()
print(f"🟢 Avg Quantity (Returned Orders): {returned_qty_avg:.2f}")
print(f"🔵 Avg Quantity (Non-Returned Orders): {non_returned_qty_avg:.2f}")

# --------------------------
# Visualizations
# --------------------------
# Monthly Return Rate
plt.figure(figsize=(10, 4))
monthly_return_rate.plot(kind='bar', color='tomato')
plt.title("Monthly Return Rate")
plt.ylabel("Return Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Returned Items
plt.figure(figsize=(10, 4))
sns.barplot(x=top_returned.values, y=top_returned.index, hue=top_returned.index, palette='Set3', dodge=False)
plt.title("Top 10 Returned Items")
plt.xlabel("Return Count")
plt.ylabel("Item Name")
plt.tight_layout()
plt.show()

# Buyer Return Rate Distribution
plt.figure(figsize=(8, 4))
sns.histplot(buyer_return_rate, bins=30, kde=True, color='purple')
plt.title("Customer Return Rate Distribution")
plt.xlabel("Return Rate per Buyer")
plt.tight_layout()
plt.show()

# Return Rate Over Time
plt.figure(figsize=(12, 5))
monthly_returns.plot(marker='o')
plt.title("Monthly Product Returns")
plt.xlabel("Month")
plt.ylabel("Number of Returns")
plt.grid(True)
plt.tight_layout()
plt.show()

# Return Rate by Product Category

plt.figure(figsize=(10, 6))
sns.barplot(x=category_return_rate.values, y=category_return_rate.index, palette='crest')
plt.xlabel("Return Rate (%)")
plt.title("Return Rate by Product Category")
plt.tight_layout()
plt.show()

# Return Rate vs. Quantity Ordered
plt.figure(figsize=(8, 5))
sns.boxplot(x='Returned', y='Final Quantity', data=df)
plt.xticks([0, 1], ['Not Returned', 'Returned'])
plt.title("Quantity Ordered vs. Return Behavior")
plt.xlabel("Order Type")
plt.ylabel("Quantity Ordered")
plt.tight_layout()
plt.show()
