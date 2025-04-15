import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Simulate a consistent test environment
np.random.seed(42)
random.seed(42)

# Generate dummy data for 6 servers
servers = ["A", "B", "C", "D", "E", "F"]
data = {
    "Server": servers,
    "Temperature": [random.randint(45, 75) for _ in servers],
    "CPU_Usage": [random.randint(30, 90) for _ in servers],
    "Response_Time": [random.randint(80, 300) for _ in servers],
    "Active_Connections": [random.randint(10, 100) for _ in servers],
    "Weight": [random.randint(1, 10) for _ in servers],  # For Weighted Round Robin
    "Client_IP": [random.randint(10000, 99999) for _ in servers]  # For IP hash
}

df = pd.DataFrame(data)

# ---------- 1. Round Robin ----------
# Round Robin is indifferent to stats; picks next in order. We'll simulate position 0 as "chosen".
df["Round_Robin_Score"] = [0] + [1] * (len(df) - 1)

# ---------- 2. Least Connections ----------
df["Least_Conn_Score"] = df["Active_Connections"]

# ---------- 3. Least Response Time ----------
df["Response_Time_Score"] = df["Response_Time"]

# ---------- 4. Weighted Round Robin ----------
# Score = 1 / weight (lower weight = less preferred)
df["Weighted_RR_Score"] = 1 / df["Weight"]

# ---------- 5. IP Hash ----------
# Simulate with hash modulus operation
df["IP_Hash_Score"] = [ip % len(servers) for ip in df["Client_IP"]]

# ---------- 6. ThermoLoad ----------
# Normalize values
for col in ["Temperature", "CPU_Usage", "Response_Time"]:
    df[col + "_Norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Custom weights
weights = {
    "Temperature_Norm": 0.5,
    "CPU_Usage_Norm": 0.3,
    "Response_Time_Norm": 0.2
}

df["ThermoLoad_Score"] = (
    df["Temperature_Norm"] * weights["Temperature_Norm"] +
    df["CPU_Usage_Norm"] * weights["CPU_Usage_Norm"] +
    df["Response_Time_Norm"] * weights["Response_Time_Norm"]
)

# Normalize all score columns so lower = better
score_cols = [
    "Round_Robin_Score", "Least_Conn_Score", "Response_Time_Score",
    "Weighted_RR_Score", "IP_Hash_Score", "ThermoLoad_Score"
]

# Normalize for fair comparison
for col in score_cols:
    norm_col = col + "_Norm"
    df[norm_col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Compute average normalized score
df["Average_Score"] = df[[col + "_Norm" for col in score_cols]].mean(axis=1)

# Display results
display_columns = ["Server", "Temperature", "CPU_Usage", "Response_Time", "Active_Connections", "Weight", "Average_Score"]
print("📊 Server Comparison Across Load Balancing Algorithms:\n")
print(df[display_columns].sort_values("Average_Score"))

# Plot comparison
plt.figure(figsize=(12, 6))
for algo in score_cols:
    plt.plot(df["Server"], df[algo + "_Norm"], marker='o', label=algo.replace("_Score", "").replace("_", " "))

plt.title("Normalized Score Comparison of Load Balancing Algorithms")
plt.ylabel("Normalized Score (Lower is Better)")
plt.xlabel("Server")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
