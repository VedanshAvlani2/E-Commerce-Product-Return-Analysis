# E-Commerce Product Return Analysis

## Overview
This project analyzes customer return behavior in an e-commerce dataset. It explores return rates, customer tendencies, top returned products, and trends over time.

## Objective
Identify key drivers behind product returns to inform product strategy and improve customer satisfaction.

## Dataset & Inputs
- **Source**: Real-world dataset provided (`order_dataset.csv`)
- **Columns**: Date, Item Name, Buyer ID, Category, Final Quantity, Refunded Item Count

## Technologies Used
- Python
- pandas, numpy
- matplotlib, seaborn

## How to Run
```bash
# Step 1: Install dependencies
pip install pandas matplotlib seaborn

# Step 2: Run the script
python Product_Return_Analysis.py
```

## Workflow
1. Load and clean dataset
2. Derive return flags and extract date information
3. Compute KPIs:
   - Total Orders
   - Return Rate
   - Top Returned Products
   - Buyer-level return rate
   - Monthly and category trends
4. Visualize insights using matplotlib and seaborn

## Results
- Monthly return rate visualized as bar chart
- Top returned products displayed using horizontal bar chart
- Return distribution by buyer and categories
- Quantity ordered vs. return behavior shown via boxplots

## Key Takeaways
- Identified high-return product categories
- Spotted peak return months
- Highlighted customer return segments (e.g., habitual returners)

## Future Enhancements
- Add return reason NLP analysis
- Integrate predictive model for return probability
- Analyze post-return purchase behavior
