import pandas as pd

# Best “happy path” import
df = pd.read_csv("f1RacesYear.csv")  # or r"C:\path\to\my_file.csv" on Windows

# Quick sanity check
print(df.head())
print(df.info())