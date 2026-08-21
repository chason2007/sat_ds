import pandas as pd

df = pd.read_csv("clean_data.csv")

#classification of moisture and solar levels
df["moisture_level"] = pd.cut(df["soil_moisture_percent"], [0, 30, 60, 100], labels=["Low", "Medium", "High"])
df["solar_level"] = pd.cut(df["solar_intensity_w_m2"], [0, 350, 700, 1000], labels=["Low", "Medium", "High"])


print("Average water use by soil moisture level:")
print(df.groupby("moisture_level")["water_use_liters"].mean())

print("\nAverage water use by solar intensity level:")
print(df.groupby("solar_level")["water_use_liters"].mean())
