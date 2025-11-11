#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a random dataset of 100 rows × 30 columns (values between [1,200])
np.random.seed(42)
data = pd.DataFrame(np.random.randint(1, 201, size=(100, 30)), columns=[f'Col_{i+1}' for i in range(30)])

print("Original Dataset (First 5 Rows):")
print(data.head())

# Replace all values between [10,60] with NaN
data_masked = data.mask((data >= 10) & (data <= 60))

# Count of NAs in each row and column
na_rows = data_masked.isna().sum(axis=1)
na_cols = data_masked.isna().sum(axis=0)

print("\nCount of NAs in Each Row:")
print(na_rows.head())
print("\nCount of NAs in Each Column:")
print(na_cols)

# Replace NA values with the average of each column
data_filled = data_masked.fillna(data_masked.mean())

# Plot Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data_filled.corr(), cmap="coolwarm", annot=False)
plt.title("Heatmap of Column Correlations")
plt.show()

# Count number of columns having correlation <= 0.7
corr_matrix = data_filled.corr()
count_low_corr = (corr_matrix.abs() <= 0.7).sum().sum()  # Count total correlations <= 0.7
# Remove self-correlations (diagonal = 1)
count_low_corr -= len(corr_matrix)
print(f"\nNumber of column correlations ≤ 0.7: {count_low_corr}")

# Normalize each column between 0 and 10
normalized_data = (data_filled - data_filled.min()) / (data_filled.max() - data_filled.min()) * 10

print("\nNormalized Dataset (0–10 Range, First 5 Rows):")
print(normalized_data.head())

# Replace all values with 0 if <=5, else 1
binary_data = normalized_data.map(lambda x: 0 if x <= 5 else 1)

print("\nBinary Transformed Dataset (0 if ≤5 else 1, First 5 Rows):")
print(binary_data.head())

# Visualize distribution
plt.figure(figsize=(8, 5))
sns.histplot(binary_data.values.flatten(), bins=2, discrete=True)
plt.title("Distribution of Binary Values (0 and 1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

