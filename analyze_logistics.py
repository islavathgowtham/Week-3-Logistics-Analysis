from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "logistics_shipments.csv"
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["shipment_date"])
print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDescriptive statistics:\n", df[[
    "distance_km", "shipment_volume_units", "delivery_hours", "transport_cost_inr"
]].describe().round(2))
print("\nCorrelation matrix:\n", df[[
    "distance_km", "shipment_volume_units", "delivery_hours", "transport_cost_inr"
]].corr().round(2))

monthly = df.assign(month=df["shipment_date"].dt.to_period("M").astype(str)).groupby("month").agg(
    shipment_count=("shipment_id", "count"),
    avg_delivery_hours=("delivery_hours", "mean"),
    avg_cost_inr=("transport_cost_inr", "mean"),
    delay_rate_pct=("delayed", lambda s: (s.eq("Yes").mean() * 100))
).reset_index()
destination = df.groupby("destination").agg(
    shipment_count=("shipment_id", "count"),
    avg_delivery_hours=("delivery_hours", "mean"),
    avg_cost_inr=("transport_cost_inr", "mean"),
    delay_rate_pct=("delayed", lambda s: s.eq("Yes").mean() * 100)
).reset_index()

# 1. Delivery-time distribution
plt.figure(figsize=(8, 4.5))
plt.hist(df["delivery_hours"], bins=12, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery time (hours)")
plt.ylabel("Number of shipments")
plt.tight_layout()
plt.savefig(OUT / "delivery_time_distribution.png", dpi=160)
plt.close()

# 2. Monthly trend
plt.figure(figsize=(8, 4.5))
plt.plot(monthly["month"], monthly["avg_delivery_hours"], marker="o")
plt.title("Monthly Average Delivery Time")
plt.xlabel("Month")
plt.ylabel("Average delivery time (hours)")
plt.xticks(rotation=30)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / "monthly_delivery_trend.png", dpi=160)
plt.close()

# 3. Destination cost comparison
plt.figure(figsize=(8, 4.5))
plt.bar(destination["destination"], destination["avg_cost_inr"], edgecolor="black")
plt.title("Average Transport Cost by Destination")
plt.xlabel("Destination")
plt.ylabel("Average cost (INR per shipment)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUT / "cost_by_destination.png", dpi=160)
plt.close()

# 4. Distance-cost relationship
plt.figure(figsize=(8, 4.5))
plt.scatter(df["distance_km"], df["transport_cost_inr"], alpha=0.8)
plt.title("Distance vs Transport Cost")
plt.xlabel("Distance (km)")
plt.ylabel("Transport cost (INR)")
plt.tight_layout()
plt.savefig(OUT / "distance_vs_cost.png", dpi=160)
plt.close()

# 5. Correlation matrix
metrics = ["distance_km", "shipment_volume_units", "delivery_hours", "transport_cost_inr"]
corr = df[metrics].corr()
plt.figure(figsize=(7, 5))
plt.imshow(corr, aspect="auto", vmin=-1, vmax=1)
plt.colorbar(label="Correlation coefficient")
labels = ["Distance", "Volume", "Delivery time", "Transport cost"]
plt.xticks(range(len(labels)), labels, rotation=30, ha="right")
plt.yticks(range(len(labels)), labels)
for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
plt.title("Correlation Matrix of Logistics Metrics")
plt.tight_layout()
plt.savefig(OUT / "correlation_matrix.png", dpi=160)
plt.close()

monthly.to_csv(OUT / "monthly_kpi_summary.csv", index=False)
destination.to_csv(OUT / "destination_kpi_summary.csv", index=False)
print("\nCharts and KPI summary files saved in:", OUT)
