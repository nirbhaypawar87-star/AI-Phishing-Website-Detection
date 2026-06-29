import pandas as pd

# Read the dataset
df = pd.read_csv("../dataset/dataset.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Info:")
print(df.info())

# Display number of rows and columns
print("\nShape:", df.shape)