# Week 3: Advanced Data Analysis and Visualization in Logistics

## 1. Project Overview

This project focuses on advanced data analysis and visualization techniques for understanding logistics operations using Python. The main objective is to explore a hypothetical logistics dataset, identify patterns in delivery performance, analyze transportation costs, and generate meaningful insights that support data-driven decision-making.

The project uses a simulated dataset containing 60 shipment records across six months. The dataset includes shipment IDs, shipment dates, origin and destination locations, carrier information, transportation distance, shipment volume, delivery duration, transportation costs, and a delay indicator.

Exploratory Data Analysis (EDA) is performed using Python libraries such as Pandas, NumPy, and Matplotlib. Descriptive statistics are calculated to understand central tendencies, data distributions, and variability. Correlation analysis is used to examine relationships between transportation distance, shipment volume, delivery time, and transportation costs.

Multiple visualizations are created to communicate the results clearly. These include a histogram showing delivery-time distribution, a line chart illustrating monthly delivery-time trends, a bar chart comparing transportation costs by destination, a scatter plot examining the relationship between distance and cost, and a correlation matrix summarizing relationships among numerical variables.

The analysis helps demonstrate how logistics teams can identify potential bottlenecks, monitor delivery performance, investigate high-cost routes, and evaluate operational efficiency. The report also provides recommendations for improving transportation planning, monitoring carrier performance, and communicating findings to stakeholders.

**Note:** The dataset and findings are simulated for educational purposes and do not represent actual company operations.

## 2. Project Objectives

- Perform exploratory data analysis on logistics shipment data.
- Calculate mean, median, standard deviation, minimum, maximum, and quartiles.
- Analyze delivery-time distributions and monthly trends.
- Examine transportation costs across different destinations.
- Investigate relationships between distance, shipment volume, delivery time, and cost.
- Create meaningful visualizations using Python.
- Interpret analytical findings and identify potential operational bottlenecks.
- Provide recommendations to support logistics decision-making.

## 3. Technologies Used

- **Python:** Data analysis and visualization programming.
- **Pandas:** Data manipulation, grouping, aggregation, and statistical summaries.
- **NumPy:** Numerical calculations.
- **Matplotlib:** Creation of charts and visualizations.
- **CSV:** Storage of shipment data.
- **GitHub:** Version control and project documentation.

## 4. Dataset Description

The dataset is stored in `data/logistics_shipments.csv`.

| Column | Description |
|---|---|
| shipment_id | Unique shipment identifier |
| shipment_date | Date the shipment was recorded |
| origin | Shipment starting location |
| destination | Shipment destination |
| carrier | Transportation service provider |
| distance_km | Transportation distance in kilometres |
| shipment_volume_units | Number of units in the shipment |
| delivery_hours | Delivery duration in hours |
| transport_cost_inr | Transportation cost in Indian rupees |
| delayed | Illustrative shipment delay indicator |

The dataset contains 60 simulated shipments covering January to June 2026.

## 5. Exploratory Data Analysis

The analysis includes the following activities:

### Descriptive Statistics

Descriptive statistics summarize the typical values and variability of delivery durations, transportation distances, shipment volumes, and transportation costs.

Mean and median values help describe typical performance, while standard deviation, minimum, maximum, and quartiles reveal variability and potentially unusual observations.

### Distribution Analysis

A histogram is used to examine the distribution of delivery durations and identify whether some shipments take considerably longer than others.

### Trend Analysis

A monthly line chart displays average delivery duration across the six-month period. This helps illustrate changes in delivery performance over time.

### Destination-Level Analysis

A bar chart compares average transportation costs across destinations. This helps identify destinations that may require further cost investigation.

### Correlation Analysis

A correlation matrix examines linear relationships between transportation distance, shipment volume, delivery duration, and transportation costs.

Correlation indicates association rather than causation, so the results must be interpreted alongside operational context.

## 6. Data Visualizations

The project includes five visualizations:

1. **Delivery-Time Distribution:** A histogram used to understand the spread of delivery durations and identify unusually long shipments.
2. **Monthly Average Delivery Time:** A line chart used to examine changes in delivery performance over time.
3. **Average Transport Cost by Destination:** A bar chart used to compare transportation costs across destinations.
4. **Distance Versus Transport Cost:** A scatter plot used to investigate the relationship between route distance and transportation expenses.
5. **Correlation Matrix:** A visual summary of linear relationships among the numerical logistics metrics.

The charts are saved in the `visualizations/` directory and embedded in the project report.

## 7. Key Analytical Insights

The analysis demonstrates how logistics data can be used to investigate:

- Differences in delivery durations across destinations.
- Monthly changes in average delivery performance.
- Potential transportation cost drivers.
- High-cost shipments that may require invoice or surcharge review.
- Relationships between transportation distance and delivery duration.
- Possible operational bottlenecks requiring further investigation.

Destination-level cost differences should be interpreted with distance, shipment volume, and carrier mix in mind. Similarly, delivery delays should be evaluated against promised delivery times or service-level agreements in real operational datasets.

All findings in this project are illustrative because the dataset is simulated.

## 8. Python Implementation

The main analysis script is available at `src/analyze_logistics.py`.

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

Run the analysis from the repository root directory:

```bash
python src/analyze_logistics.py
```

The script calculates descriptive statistics and correlations, generates the visualizations, and saves monthly and destination-level KPI summaries.

## 9. Expected Outputs

The project generates the following outputs:

- Delivery-time distribution chart.
- Monthly delivery-time trend chart.
- Destination-level transportation cost chart.
- Distance-versus-cost scatter plot.
- Correlation matrix.
- Monthly KPI summary CSV file.
- Destination KPI summary CSV file.
- Detailed Word report with charts, interpretations, and recommendations.

## 10. Business Applications

The techniques demonstrated in this project can support:

- Delivery performance monitoring.
- Transportation cost analysis.
- Route and carrier evaluation.
- Identification of unusual delivery durations.
- Operational bottleneck investigation.
- Logistics KPI reporting.
- Data-driven transportation planning.

The findings can be communicated through dashboards, periodic performance reports, and management summaries to help teams prioritize operational improvements.

## 11. Recommendations

Based on the analytical approach demonstrated in this project:

- Monitor average and median delivery durations regularly.
- Investigate unusually long deliveries using route and carrier records.
- Compare transportation costs using cost per kilometre and cost per unit.
- Evaluate carriers using comparable routes and service commitments.
- Review unusual transportation charges against invoices and surcharges.
- Track monthly KPIs alongside shipment volumes and destination mix.
- Define delay metrics consistently using promised delivery times or service-level agreements.

These recommendations should be validated using actual operational data before implementation.

## 12. Limitations

- The dataset contains simulated shipment records rather than real company data.
- The sample includes only 60 shipments across six months.
- The delay indicator is a simplified educational measure.
- Transportation costs depend on several factors beyond distance.
- Correlation analysis does not establish causation.
- Real operational decisions require validated data and additional business context.

## 13. Conclusion

This project demonstrates how exploratory data analysis and visualization can help explain logistics performance and support informed operational decisions. Descriptive statistics summarize shipment characteristics, charts reveal trends and distributions, and correlation analysis helps investigate relationships between important logistics metrics.

The analysis provides a structured foundation for identifying potential delivery bottlenecks, investigating transportation costs, and monitoring operational efficiency. Python-based analytical workflows also make the process easier to reproduce and extend.

Overall, the project highlights the value of data-driven decision-making in logistics and provides a foundation for future work involving larger datasets, predictive modelling, route optimization, and business intelligence dashboards.

## 14. Project Structure

```text
Week-3-Logistics-Analysis/
├── README.md
├── requirements.txt
├── data/
│   └── logistics_shipments.csv
├── src/
│   └── analyze_logistics.py
├── visualizations/
│   ├── delivery_time_distribution.png
│   ├── monthly_delivery_trend.png
│   ├── cost_by_destination.png
│   ├── distance_vs_cost.png
│   ├── correlation_matrix.png
│   ├── monthly_kpi_summary.csv
│   └── destination_kpi_summary.csv
└── report/
    └── Week_3_Advanced_Logistics_Analysis_Report.docx
```

## 15. References

- Pandas Documentation: https://pandas.pydata.org/docs/
- NumPy Documentation: https://numpy.org/doc/
- Matplotlib Documentation: https://matplotlib.org/stable/

---

**Project Title:** Advanced Data Analysis and Visualization in Logistics  
**Task:** Week 3  
**Purpose:** Educational demonstration of logistics data analysis using Python  
**Dataset:** Simulated logistics shipment data
