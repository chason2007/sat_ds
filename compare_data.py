import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_data.csv")

#classification of moisture and solar levels
df["moisture_level"] = pd.cut(df["soil_moisture_percent"], [0, 30, 60, 100], labels=["Low", "Medium", "High"])
df["solar_level"] = pd.cut(df["solar_intensity_w_m2"], [0, 350, 700, 1000], labels=["Low", "Medium", "High"])

moisture = df.groupby("moisture_level")["water_use_liters"].mean()
solar = df.groupby("solar_level")["water_use_liters"].mean()

fig, ax = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

bars1 = ax[0].bar(moisture.index.astype(str), moisture.values, color="steelblue")
ax[0].set_title("Average water use by soil moisture level")
ax[0].set_xlabel("Soil moisture level")
ax[0].set_ylabel("Average water use (liters)")
ax[0].bar_label(bars1, fmt="%.1f")

bars2 = ax[1].bar(solar.index.astype(str), solar.values, color="steelblue")
ax[1].set_title("Average water use by solar intensity level")
ax[1].set_xlabel("Solar intensity level")
ax[1].bar_label(bars2, fmt="%.1f")

plt.tight_layout()
plt.savefig("step3_chart.png")
plt.show()
