# ============================================
# 📊 Exploratory Data Analysis (EDA) Project
# ============================================

# 👩‍🎓 Name: Ayushi Deshmukh
# 📘 Project: Real-world Data Analysis (Retail Dataset)

# ============================================
# 1. Import Libraries
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ============================================
# 2. Load Dataset
# ============================================

# Make sure 'data.csv' is in same folder
df = pd.read_csv("data.csv")

print("\n🔹 First 5 Rows:")
print(df.head())

# ============================================
# 3. Data Understanding
# ============================================

print("\n🔹 Dataset Info:")
df.info()

print("\n🔹 Statistical Summary:")
print(df.describe())

print("\n🔹 Missing Values:")
print(df.isnull().sum())

# ============================================
# 4. Data Cleaning
# ============================================

# Remove missing values
df.dropna(inplace=True)

print("\n🔹 After Cleaning:")
print(df.isnull().sum())

# Convert Order Date to datetime
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])

# ============================================
# 5. Data Analysis & Visualization
# ============================================

# 📌 1. Sales by Category
plt.figure(figsize=(6,4))
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# 📌 2. Profit by Region
plt.figure(figsize=(6,4))
df.groupby("Region")["Profit"].sum().plot(kind="bar")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()

# 📌 3. Sales Trend (First 50 records)
if 'Order Date' in df.columns:
    plt.figure(figsize=(8,4))
    df.sort_values('Order Date').head(50).plot(x='Order Date', y='Sales')
    plt.title("Sales Trend Over Time")
    plt.show()

# 📌 4. Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.c
