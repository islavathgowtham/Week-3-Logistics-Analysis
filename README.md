# Week 3: Advanced Data Analysis and Visualization in Logistics

## Project Overview
This project explores a hypothetical logistics dataset using Python. It applies exploratory data analysis (EDA), descriptive statistics, correlation analysis, and visualizations to investigate delivery performance, shipment volume, transport costs, and possible operational bottlenecks.

The dataset contains 60 simulated shipments between Hyderabad and five destination areas. It includes shipment dates, destinations, carriers, distances, shipment volumes, delivery times, transport costs, and a delay indicator. All data is synthetic and intended for educational demonstration only.

## Objectives
- Explore the structure and quality of logistics data.
- Calculate central tendencies and descriptive statistics.
- Analyze relationships among distance, volume, delivery time, and cost.
- Create multiple charts and interpret operational implications.
- Develop evidence-based recommendations for logistics decision-making.

## Tools
Python, Pandas, NumPy, Matplotlib, CSV, GitHub.

## Repository Structure
- `data/logistics_shipments.csv` — simulated shipment records.
- `src/analyze_logistics.py` — EDA and visualization script.
- `visualizations/` — generated charts and KPI summaries.
- `report/Week_3_Advanced_Logistics_Analysis_Report.docx` — detailed report.
- `requirements.txt` — Python dependencies.

## How to Run
From the repository root:

```bash
pip install -r requirements.txt
python src/analyze_logistics.py
```

The script prints descriptive statistics and a correlation matrix, then generates charts and KPI summaries in `visualizations/`.

## Visualizations
1. Delivery-time histogram — shows the distribution and potential long-delivery tail.
2. Monthly average delivery time — highlights changes over time.
3. Average cost by destination — compares route cost profiles.
4. Distance vs transport cost scatter plot — examines the relationship between route length and cost.
5. Correlation matrix — summarizes linear associations among numerical metrics.

## Interpretation and Use
The charts help logistics teams identify high-cost destinations, monitor changes in delivery speed, inspect unusual delivery times, and understand cost drivers. Correlation indicates association, not causation; operational decisions should also consider carrier service levels, route conditions, shipment type, and data limitations.

## Data Disclaimer
All shipment records are simulated for learning purposes. Findings are illustrative and should not be presented as actual company performance.
