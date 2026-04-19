Monthly Business Performance Report 

How can we quickly evaluate performance across product categories and identify the most profitable and least efficient transactions?

monthly_data.csv

*Dataset*
Columns:
category
revenue 
cost

*Metrics Created*
profit = revenue - cost
margin = profit / revenue 
weighted_margin = total_profit / total_revenue 

*Process*
1. Load the dataset using pandas
2. Derive profit and margin metrics
3. Aggregate performance by category
4. Calculate weighted margin
5. Identify the top profit transactions
6. Identify the worst margin transactions 
7. Export structured reports 

*Outputs*
category_summary.csv
top_profit_rows.csv
worst_margin_rows.csv

*Business Insight*
Category C generated the highest total profit and strongest margin, suggesting strong pricing efficiency. 
Category A produced significant fiscal loss, revealing a potential cost structure or pricing issue that would require investigation. 


Time-Based Analysis

This project aggregates monthly revenue and profit trends over time. 
A 3 month moving average was applied to smooth short-term volatility. 
Next-month profit was estimated using average of the most recent 3 months. 

Business Insight

Profit appears volatile month to month, but the moving average suggests a more stable baseline level of performance.
The forecast estimate provides a simple planning reference for the next reporting period. 