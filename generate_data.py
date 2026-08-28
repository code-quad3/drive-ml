import random
import pandas as pd

data = []

for _ in range(5000):
    distance = random.uniform(0.5, 10)
    hour = random.randint(0, 23)
    day_of_week = random.randint(0, 6)

    if 8 <= hour <= 10:
        traffic_factor = 1.5
    elif 17 <= hour <= 20:
        traffic_factor = 1.7
    else:
        traffic_factor = 1.0

    eta = distance * 3 * traffic_factor + random.uniform(-1, 1)

    data.append([
        distance,
        hour,
        day_of_week,
        max(1, eta)
    ])

df = pd.DataFrame(
    data,
    columns=[
        "distance_km",
        "hour",
        "day_of_week",
        "eta_minutes"
    ]
)

df.to_csv("eta_dataset.csv", index=False)

print(df.head())
print("Rows:", len(df))