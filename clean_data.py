import pandas as pd

df = pd.read_csv("Q34_smart_irrigation.csv")

#removing duplicate records
print("Repeated cycles:", df.duplicated().sum())
df = df.drop_duplicates()

#filling missing values with median value 
df["soil_moisture_percent"] = df["soil_moisture_percent"].fillna(df["soil_moisture_percent"].median())
df["water_use_liters"] = df["water_use_liters"].fillna(df["water_use_liters"].median())

df.to_csv("clean_data.csv", index=False)
