# Data Analytics Fundamentals

> Professional Python for Data Analytics

This project comes with professional documentation.

Explore the tabs and sidebars for content.

This is where we present our analytics work.

See:

- [Resources](./RESOURCES.md)
- [Troubleshooting](./TROUBLESHOOTING.md)

---

## Custom Project

### Dataset
This project uses Seaborn’s built-in tips dataset, which includes restaurant billing data like total bill, tip amount, party size, and some context like day of the week, time of day, and customer info. It’s a nice mix of numeric and categorical data, so it works well for practicing basic EDA and feature engineering.

### Signals
I used both the original dataset columns and a couple of engineered features:
- Numeric columns: total_bill, tip, size
- Categorical columns: day, time, sex, smoker
- New features I created:
  - `spending_category` (Low, Medium, High based on total bill)
  - `bill_vs_day_avg` (compares each bill to the average bill for that day)

These added features helped give a little more context to spending behavior instead of just looking at raw numbers.

### Experiments
I did two main feature engineering steps:

- First, I binned total bill into a simple spending_category so it’s easier to see low vs high spenders at a glance.
- Then I created bill_vs_day_avg, which compares each transaction to the average bill for that specific day. This helps show whether a bill is above or below “normal” for that day.

### Results
A few clear patterns showed up pretty quickly. There’s a solid positive relationship between total bill and tip, meaning bigger bills usually lead to bigger tips. Party size also seems to have some influence on spending.

The bill_vs_day_avg feature mostly centers around 1, which makes sense since it’s a ratio. It basically shows that most transactions are pretty close to the daily average, with some higher and lower outliers. The spending categories also helped make it easier to quickly spot low vs high spend transactions.

### Interpretation
Overall, the main takeaway is that total bill size is the strongest driver of tip amount. Day of the week doesn’t really change behavior that much.

The derived features helped make the data a bit easier to interpret. Instead of just raw values, I can now see relative spending patterns and group customers into clearer segments.

From a business perspective, it looks like increasing order size is more closely tied to higher tips than anything else in the dataset.
