import pandas as pd

df = pd.read_csv("clean_data.csv")

#water-use efficiency = liters of water per minute of pump runtime
df["water_use_efficiency"] = df["water_use_liters"] / df["pump_runtime_min"]

print("Water use efficiency:")
print(df["water_use_efficiency"].describe())

#classify irrigation demand from soil moisture and solar intensity
def get_demand(row):
    if row["soil_moisture_percent"] < 30 and row["solar_intensity_w_m2"] > 350:
        return "High"
    elif row["soil_moisture_percent"] < 60:
        return "Moderate"
    else:
        return "Low"

df["irrigation_demand"] = df.apply(get_demand, axis=1)

print("\nNumber of cycles in each demand class:")
print(df["irrigation_demand"].value_counts())

print("\nAverage water use by demand class:")
print(df.groupby("irrigation_demand")["water_use_liters"].mean())

print("\nAverage efficiency by demand class:")
print(df.groupby("irrigation_demand")["water_use_efficiency"].mean())

df.to_csv("final_data.csv", index=False)
