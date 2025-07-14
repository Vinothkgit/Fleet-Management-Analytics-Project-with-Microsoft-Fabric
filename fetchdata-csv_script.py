import requests
import pandas as pd
import random
import os
from datetime import datetime

# Step 1: Fetch live transit data from MBTA API
def fetch_mbta_data():
    url = "https://api-v3.mbta.com/vehicles"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["data"]
        records = []
        for item in data:
            attr = item.get("attributes", {})
            records.append({
                "vehicle_id": item.get("id"),
                "latitude": attr.get("latitude"),
                "longitude": attr.get("longitude"),
                "bearing": attr.get("bearing"),
                "current_status": attr.get("current_status"),
                "speed": attr.get("speed"),
                "timestamp": attr.get("updated_at")
            })
        return pd.DataFrame(records)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Step 2: Enrich data with simulated IoT metrics and metadata
def enrich_data(df):
    vehicle_types = ['bus', 'truck', 'van', 'car', 'bike']
    location_names = ['Boston', 'Cambridge', 'Somerville', 'Newton', 'Quincy']
    congestion_levels = ['Low', 'Medium', 'High']

    df["fuel_level"] = [round(random.uniform(10, 100), 2) for _ in range(len(df))]
    df["engine_temp"] = [round(random.uniform(60, 120), 2) for _ in range(len(df))]
    df["driver_id"] = [f"DVR{random.randint(1000, 9999)}" for _ in range(len(df))]
    df["alert_flag"] = df["fuel_level"].apply(lambda x: 1 if x < 20 else 0)
    df["vehicle_type"] = [random.choice(vehicle_types) for _ in range(len(df))]
    df["location_name"] = [random.choice(location_names) for _ in range(len(df))]
    df["tire_pressure"] = [round(random.uniform(28, 36), 1) for _ in range(len(df))]
    df["route_congestion_level"] = [random.choice(congestion_levels) for _ in range(len(df))]
    df["traffic_incident"] = [random.choice([0, 1]) for _ in range(len(df))]  # 0: no incident, 1: incident
    df["ingested_at"] = datetime.utcnow().isoformat()
    return df

# Step 3: Overwrite local CSV file
def save_to_csv(df, path="fleet_latest.csv"):
    if os.path.exists(path):
        os.remove(path)  # Delete old file
    df.to_csv(path, index=False)
    print(f"✅ Data saved to {path}")

# Run all steps
if __name__ == "__main__":
    df_raw = fetch_mbta_data()
    df_enriched = enrich_data(df_raw)
    save_to_csv(df_enriched)
